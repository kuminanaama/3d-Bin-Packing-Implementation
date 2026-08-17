import time
from src.models.box import Box
from src.models.container import Container
from src.algorithms.milp_algorithm import MILPAlgorithm


container = Container(length=10, width=6, height=5)

boxes = [
    Box("box1", length=6, width=5, height=4),
    Box("box2", length=5, width=4, height=3),
    Box("box3", length=3, width=5, height=2)
]

algorithm = MILPAlgorithm(container, boxes)

#calaculate runtime
start_time = time.perf_counter()

packed_boxes, unpacked_boxes, placements = algorithm.solve()

end_time = time.perf_counter()

runtime = end_time - start_time


print()
print(f"Packed boxes: {[box.box_id for box in packed_boxes]}")
print(f"Unpacked boxes: {[box.box_id for box in unpacked_boxes]}")

print("\nPlacements:")
for placement in placements:
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

# Calculate container utilisation
total_packed_volume = sum(
    placement.placed_length
    * placement.placed_width
    * placement.placed_height
    for placement in placements
)

container_volume = (
    container.length
    * container.width
    * container.height
)

utilisation = (total_packed_volume / container_volume) * 100

print(f"\nContainer Utilisation: {utilisation:.2f}%")

print(f"Runtime: {runtime:.6f} seconds")