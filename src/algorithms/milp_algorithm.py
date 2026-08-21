import pulp

from src.models.box import Box
from src.models.container import Container
from src.models.placement import Placement


class MILPAlgorithm:
    def __init__(self, container: Container, boxes: list[Box]):
        self.container = container
        self.boxes = boxes

    def solve(self):
        # Create the optimization problem
        prob = pulp.LpProblem("3D_Bin_Packing", pulp.LpMaximize)

        # Binary selection variables
        # 1 = box is selected, 0 = box is not selected
        box_vars = [
            pulp.LpVariable(f"box_{i}", cat="Binary")
            for i in range(len(self.boxes))
        ]

        # Objective: maximise packed volume
        prob += pulp.lpSum(
            box_vars[i] * self.boxes[i].volume()
            for i in range(len(self.boxes))
        ), "MaximizeVolume"

        # Orientation variables
        orientation_vars = {}

        # Dimensions chosen for each box
        chosen_length = {}
        chosen_width = {}
        chosen_height = {}

        for i, box in enumerate(self.boxes):
            orientations = box.orientations()

            # Create a binary variable for each possible orientation
            for o in range(len(orientations)):
                orientation_vars[i, o] = pulp.LpVariable(
                    f"orientation_{i}_{o}",
                    cat="Binary"
                )

            # Exactly one orientation if the box is selected
            prob += (
                pulp.lpSum(
                    orientation_vars[i, o]
                    for o in range(len(orientations))
                )
                == box_vars[i]
            ), f"OneOrientation_{i}"

            # Dimensions resulting from selected orientation
            chosen_length[i] = pulp.lpSum(
                orientations[o][0] * orientation_vars[i, o]
                for o in range(len(orientations))
            )

            chosen_width[i] = pulp.lpSum(
                orientations[o][1] * orientation_vars[i, o]
                for o in range(len(orientations))
            )

            chosen_height[i] = pulp.lpSum(
                orientations[o][2] * orientation_vars[i, o]
                for o in range(len(orientations))
            )

        # Position variables
        x_vars = [
            pulp.LpVariable(f"x_{i}", lowBound=0)
            for i in range(len(self.boxes))
        ]

        y_vars = [
            pulp.LpVariable(f"y_{i}", lowBound=0)
            for i in range(len(self.boxes))
        ]

        z_vars = [
            pulp.LpVariable(f"z_{i}", lowBound=0)
            for i in range(len(self.boxes))
        ]

        # Big-M value
        M = max(
            self.container.length,
            self.container.width,
            self.container.height
        )

        # Boundary constraints
        for i in range(len(self.boxes)):
            prob += (
                x_vars[i] + chosen_length[i]
                <= self.container.length
                + M * (1 - box_vars[i])
            ), f"LengthConstraint_{i}"

            prob += (
                y_vars[i] + chosen_width[i]
                <= self.container.width
                + M * (1 - box_vars[i])
            ), f"WidthConstraint_{i}"

            prob += (
                z_vars[i] + chosen_height[i]
                <= self.container.height
                + M * (1 - box_vars[i])
            ), f"HeightConstraint_{i}"

        # Binary variables for non-overlap relationships
        left = {}
        right = {}
        front = {}
        behind = {}
        below = {}
        above = {}

        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                left[i, j] = pulp.LpVariable(
                    f"left_{i}_{j}",
                    cat="Binary"
                )

                right[i, j] = pulp.LpVariable(
                    f"right_{i}_{j}",
                    cat="Binary"
                )

                front[i, j] = pulp.LpVariable(
                    f"front_{i}_{j}",
                    cat="Binary"
                )

                behind[i, j] = pulp.LpVariable(
                    f"behind_{i}_{j}",
                    cat="Binary"
                )

                below[i, j] = pulp.LpVariable(
                    f"below_{i}_{j}",
                    cat="Binary"
                )

                above[i, j] = pulp.LpVariable(
                    f"above_{i}_{j}",
                    cat="Binary"
                )

                # Box i is left of box j
                prob += (
                    x_vars[i] + chosen_length[i]
                    <= x_vars[j]
                    + M * (1 - left[i, j])
                )

                # Box i is right of box j
                prob += (
                    x_vars[j] + chosen_length[j]
                    <= x_vars[i]
                    + M * (1 - right[i, j])
                )

                # Box i is in front of box j
                prob += (
                    y_vars[i] + chosen_width[i]
                    <= y_vars[j]
                    + M * (1 - front[i, j])
                )

                # Box i is behind box j
                prob += (
                    y_vars[j] + chosen_width[j]
                    <= y_vars[i]
                    + M * (1 - behind[i, j])
                )

                # Box i is below box j
                prob += (
                    z_vars[i] + chosen_height[i]
                    <= z_vars[j]
                    + M * (1 - below[i, j])
                )

                # Box i is above box j
                prob += (
                    z_vars[j] + chosen_height[j]
                    <= z_vars[i]
                    + M * (1 - above[i, j])
                )

                # If both boxes are selected, at least one
                # separating relationship must hold
                prob += (
                    left[i, j]
                    + right[i, j]
                    + front[i, j]
                    + behind[i, j]
                    + below[i, j]
                    + above[i, j]
                    >= box_vars[i] + box_vars[j] - 1
                )

        # Solve the MILP problem
        prob.solve(
            pulp.PULP_CBC_CMD(
                msg=False,
                timeLimit=60
            )
        )

        # Keep solver status information available
        status = pulp.LpStatus[prob.status]

        solution_status = pulp.LpSolution.get(
            prob.sol_status,
            "Unknown"
        )

        # Create lists for packed and unpacked boxes
        packed_boxes = []
        unpacked_boxes = []
        placements = []

        for i, box in enumerate(self.boxes):
            if pulp.value(box_vars[i]) == 1:
                packed_boxes.append(box)

                orientations = box.orientations()
                selected_orientation = None

                for o in range(len(orientations)):
                    if pulp.value(orientation_vars[i, o]) == 1:
                        selected_orientation = orientations[o]
                        break

                placed_length, placed_width, placed_height = (
                    selected_orientation
                )

                placement = Placement(
                    box=box,
                    x=pulp.value(x_vars[i]),
                    y=pulp.value(y_vars[i]),
                    z=pulp.value(z_vars[i]),
                    placed_length=placed_length,
                    placed_width=placed_width,
                    placed_height=placed_height
                )

                placements.append(placement)

            else:
                unpacked_boxes.append(box)

        return packed_boxes, unpacked_boxes, placements