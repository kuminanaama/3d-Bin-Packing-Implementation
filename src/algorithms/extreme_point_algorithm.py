from src.models.box import Box
from src.models.container import Container
from src.models.placement import Placement
from src.utils.extreme_point_manager import ExtremePointManager


class ExtremePointAlgorithm:
    def __init__(self, container: Container):
        self.container = container
        self.extreme_point_manager = ExtremePointManager()

    def place_box(self, box: Box) -> bool:
        for point in self.extreme_point_manager.extreme_points:
            for orientation in box.orientations():
                placed_length, placed_width, placed_height = orientation

                placement = Placement(
                    box=box,
                    x=point.x,
                    y=point.y,
                    z=point.z,
                    placed_length=placed_length,
                    placed_width=placed_width,
                    placed_height=placed_height
                )

                if self.container.can_place(placement):
                    self.container.add_placement(placement)

                    self.extreme_point_manager.update_extreme_points(
                        point,
                        placement
                    )

                    return True

        return False

    def pack_boxes(self, boxes: list[Box]):
        packed_boxes = []
        unpacked_boxes = []

        sorted_boxes = sorted(boxes, key=lambda box: box.volume(), reverse=True)

        for box in sorted_boxes:
            if self.place_box(box):
                packed_boxes.append(box)
            else:
                unpacked_boxes.append(box)

        return packed_boxes, unpacked_boxes

    def calculate_utilisation(self) -> float:
        container_volume = self.container.length * self.container.width * self.container.height
        total_packed_volume = sum(
            placement.placed_length * placement.placed_width * placement.placed_height
            for placement in self.container.placements
        )
        return total_packed_volume / container_volume * 100 