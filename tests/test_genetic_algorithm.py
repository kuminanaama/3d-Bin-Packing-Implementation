import time

from src.models.box import Box
from src.models.container import Container
from src.algorithms.genetic_algorithm import GeneticAlgorithm


container = Container(
    length=10,
    width=10,
    height=5
)

boxes = [
    Box("box1", 6, 10, 5),   # volume 300
    Box("box2", 5, 6, 5),    # volume 150
    Box("box3", 5, 4, 5),    # volume 100
    Box("box4", 4, 4, 5)     # volume 80
]

ga = GeneticAlgorithm(
    container=container,
    boxes=boxes,
    population_size=10,
    generations=50,
    mutation_rate=0.1
)

# Measure GA runtime
start_time = time.perf_counter()

(
    best_chromosome,
    best_fitness,
    packed_boxes,
    unpacked_boxes,
    placements
) = ga.run()

end_time = time.perf_counter()

runtime = end_time - start_time

# Calculate container utilisation
container_volume = (
    container.length
    * container.width
    * container.height
)

best_utilisation = (
    best_fitness / container_volume
) * 100

# Display results
print("Best chromosome:")
print([box.box_id for box in best_chromosome])

print(f"\nBest fitness: {best_fitness}")

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

print(f"\nBest utilisation: {best_utilisation:.2f}%")
print(f"Runtime: {runtime:.6f} seconds")