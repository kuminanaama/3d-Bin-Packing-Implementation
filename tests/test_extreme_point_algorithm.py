from src.models.box import Box
from src.models.container import Container
from src.algorithms.extreme_point_algorithm import ExtremePointAlgorithm
import time

container = Container(length=10, width=10, height=10)

algorithm = ExtremePointAlgorithm(container)

box1 = Box("box1", length=5, width=3, height=2)
box2 = Box("box2", length=3, width=3, height=2)
box3 = Box("box3", length=2, width=2, height=2)


boxes = [box3, box1, box2]

start_time = time.perf_counter()

packed_boxes, unpacked_boxes = algorithm.pack_boxes(boxes)

end_time = time.perf_counter()

runtime = end_time - start_time


utilisation = algorithm.calculate_utilisation()

print(f"Packed boxes: {[box.box_id for box in packed_boxes]}")
print(f"Unpacked boxes: {[box.box_id for box in unpacked_boxes]}")
print(f"\nContainer Utilisation: {utilisation:.2f}%")
print(f"Runtime: {runtime:.6f} seconds")


print("\nPlacements:")

for placement in container.placements:
    print(
        f"Box {placement.box.box_id} placed at "
        f"({placement.x}, {placement.y}, {placement.z})"
    )

    print(
        f"Orientation: "
        f"{placement.placed_length} x "
        f"{placement.placed_width} x "
        f"{placement.placed_height}"
    )

