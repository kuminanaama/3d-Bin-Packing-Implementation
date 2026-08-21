import time
from src.algorithms.extreme_point_algorithm import ExtremePointAlgorithm
from src.algorithms.milp_algorithm import MILPAlgorithm
from src.algorithms.genetic_algorithm import GeneticAlgorithm
from src.models.box import Box
from src.models.container import Container


# Common container used by all algorithms
container = Container(
    length=10,
    width=10,
    height=10
)

# Common set of boxes
boxes = [
    Box("box1", 6, 6, 6),    # 216
    Box("box2", 5, 5, 5),    # 125
    Box("box3", 4, 5, 6),    # 120
    Box("box4", 4, 4, 5),    # 80
    Box("box5", 3, 5, 5),    # 75
    Box("box6", 5, 4, 4),    # 80
    Box("box7", 3, 4, 6),    # 72
    Box("box8", 4, 3, 5),    # 60
    Box("box9", 3, 3, 4),    # 36
    Box("box10", 2, 5, 4),   # 40
    Box("box11", 5, 5, 4),   # 100
    Box("box12", 4, 4, 4),   # 64
    Box("box13", 3, 6, 4),   # 72
    Box("box14", 5, 3, 4),   # 60
    Box("box15", 3, 3, 5),   # 45
    Box("box16", 4, 5, 3),   # 60
    Box("box17", 2, 6, 4),   # 48
    Box("box18", 3, 4, 3),   # 36
    Box("box19", 5, 2, 4),   # 40
    Box("box20", 2, 3, 5)    # 30
]


# ----- Extreme Point --------------

ep_container = Container(
    length=container.length,
    width=container.width,
    height=container.height
)

ep_algorithm = ExtremePointAlgorithm(ep_container)

start_time = time.perf_counter()

packed_boxes, unpacked_boxes = ep_algorithm.pack_boxes(boxes)

end_time = time.perf_counter()

ep_runtime = end_time - start_time

#------ Utilisation------
ep_packed_volume = sum(
    placement.placed_length
    * placement.placed_width
    * placement.placed_height
    for placement in ep_container.placements
)

container_volume = (
    container.length
    * container.width
    * container.height
)

ep_utilisation = (
    ep_packed_volume / container_volume
) * 100

print("\n" + "=" * 50)
print("EXTREME POINT")
print("=" * 50)

print(f"Packed volume: {ep_packed_volume}")
print(f"Utilisation: {ep_utilisation:.2f}%")
print(f"Boxes packed: {len(packed_boxes)}")
print(f"Boxes unpacked: {len(unpacked_boxes)}")
print(f"Runtime: {ep_runtime:.6f} seconds")

# ------------- MILP ---------------------

milp_container = Container(
    length=container.length,
    width=container.width,
    height=container.height
)

milp_algorithm = MILPAlgorithm(
    container=milp_container,
    boxes=boxes
)

print("\n" + "=" * 50)
print("MILP")
print("=" * 50)

start_time = time.perf_counter()

(
    milp_packed_boxes,
    milp_unpacked_boxes,
    milp_placements
) = milp_algorithm.solve()

end_time = time.perf_counter()

milp_runtime = end_time - start_time

#------- Utilisation------

milp_packed_volume = sum(
    placement.placed_length
    * placement.placed_width
    * placement.placed_height
    for placement in milp_placements
)

milp_utilisation = (
    milp_packed_volume / container_volume
) * 100



print(f"Packed volume: {milp_packed_volume}")
print(f"Utilisation: {milp_utilisation:.2f}%")
print(f"Boxes packed: {len(milp_packed_boxes)}")
print(f"Boxes unpacked: {len(milp_unpacked_boxes)}")
print(f"Runtime: {milp_runtime:.6f} seconds")


# ----- GENETIC ALGORITHM: MULTIPLE RUNS -----

print("\n" + "=" * 50)
print("GENETIC ALGORITHM - 10 RUNS")
print("=" * 50)

ga_runs = 10

ga_fitness_results = []
ga_utilisation_results = []
ga_runtime_results = []

for run in range(ga_runs):

    ga_container = Container(
        length=container.length,
        width=container.width,
        height=container.height
    )

    ga_algorithm = GeneticAlgorithm(
        container=ga_container,
        boxes=boxes,
        population_size=20,
        generations=50,
        mutation_rate=0.1
    )

    start_time = time.perf_counter()

    (
        best_chromosome,
        best_fitness,
        packed_boxes,
        unpacked_boxes,
        placements
    ) = ga_algorithm.run()

    end_time = time.perf_counter()

    runtime = end_time - start_time

    utilisation = (
        best_fitness / container_volume
    ) * 100

    ga_fitness_results.append(best_fitness)
    ga_utilisation_results.append(utilisation)
    ga_runtime_results.append(runtime)

    print(
        f"Run {run + 1}: "
        f"Fitness = {best_fitness}, "
        f"Utilisation = {utilisation:.2f}%, "
        f"Runtime = {runtime:.6f}s"
    )


# ----- GA SUMMARY -----

average_fitness = (
    sum(ga_fitness_results) / ga_runs
)

average_utilisation = (
    sum(ga_utilisation_results) / ga_runs
)

average_runtime = (
    sum(ga_runtime_results) / ga_runs
)

best_utilisation = max(ga_utilisation_results)
worst_utilisation = min(ga_utilisation_results)

print("\n" + "-" * 50)
print("GA SUMMARY")
print("-" * 50)

print(f"Average fitness: {average_fitness:.2f}")
print(f"Average utilisation: {average_utilisation:.2f}%")
print(f"Best utilisation: {best_utilisation:.2f}%")
print(f"Worst utilisation: {worst_utilisation:.2f}%")
print(f"Average runtime: {average_runtime:.6f} seconds")