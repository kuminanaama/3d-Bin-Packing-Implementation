import matplotlib.pyplot as plt

from src.models.box import Box
from src.models.container import Container
from src.algorithms.extreme_point_algorithm import ExtremePointAlgorithm
from src.algorithms.milp_algorithm import MILPAlgorithm
from src.algorithms.genetic_algorithm import GeneticAlgorithm


def plot_packing(
    container,
    placements,
    title,
    packed_volume,
    total_boxes,
    output_file
):
    container_volume = (
        container.length
        * container.width
        * container.height
    )

    utilisation = (
        packed_volume / container_volume
    ) * 100

    fig = plt.figure(figsize=(10, 8))

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    cmap = plt.colormaps["tab20"]

    for i, placement in enumerate(placements):
        x = placement.x
        y = placement.y
        z = placement.z

        length = placement.placed_length
        width = placement.placed_width
        height = placement.placed_height

        colour = cmap(i % 20)

        ax.bar3d(
            x,
            y,
            z,
            length,
            width,
            height,
            color=colour,
            alpha=0.55,
            edgecolor="black",
            linewidth=0.8
        )

        ax.text(
            x + length / 2,
            y + width / 2,
            z + height / 2,
            placement.box.box_id,
            ha="center",
            va="center",
            fontsize=8,
            weight="bold"
        )

    ax.set_xlim(0, container.length)
    ax.set_ylim(0, container.width)
    ax.set_zlim(0, container.height)

    ax.set_xlabel("Length (X)")
    ax.set_ylabel("Width (Y)")
    ax.set_zlabel("Height (Z)")

    ax.set_xticks(range(0, container.length + 1, 2))
    ax.set_yticks(range(0, container.width + 1, 2))
    ax.set_zticks(range(0, container.height + 1, 2))

    ax.view_init(
        elev=25,
        azim=45
    )

    ax.set_box_aspect(
        (
            container.length,
            container.width,
            container.height
        )
    )

    ax.set_title(
        f"{title}\n"
        f"Packed Volume = {packed_volume} | "
        f"Utilisation = {utilisation:.2f}% | "
        f"Boxes Packed = {len(placements)}/{total_boxes}",
        pad=20
    )

    plt.tight_layout()

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()


# --------------------------------------------------
# 20 BOXES EXPERIMENT
# --------------------------------------------------

boxes = [
    Box("box1", 6, 6, 6),
    Box("box2", 5, 5, 5),
    Box("box3", 4, 5, 6),
    Box("box4", 4, 4, 5),
    Box("box5", 3, 5, 5),
    Box("box6", 5, 4, 4),
    Box("box7", 3, 4, 6),
    Box("box8", 4, 3, 5),
    Box("box9", 3, 3, 4),
    Box("box10", 2, 5, 4),
    Box("box11", 5, 5, 4),
    Box("box12", 4, 4, 4),
    Box("box13", 3, 6, 4),
    Box("box14", 5, 3, 4),
    Box("box15", 3, 3, 5),
    Box("box16", 4, 5, 3),
    Box("box17", 2, 6, 4),
    Box("box18", 3, 4, 3),
    Box("box19", 5, 2, 4),
    Box("box20", 2, 3, 5)
]


# --------------------------------------------------
# EXTREME POINT
# --------------------------------------------------

ep_container = Container(
    length=10,
    width=10,
    height=10
)

ep_algorithm = ExtremePointAlgorithm(ep_container)

ep_packed_boxes, ep_unpacked_boxes = (
    ep_algorithm.pack_boxes(boxes)
)

ep_placements = ep_container.placements

ep_packed_volume = sum(
    box.volume()
    for box in ep_packed_boxes
)

plot_packing(
    ep_container,
    ep_placements,
    "Extreme Point 3D Packing Solution",
    ep_packed_volume,
    len(boxes),
    "results/ep_20_boxes_packing.png"
)


# --------------------------------------------------
# MILP
# --------------------------------------------------

milp_container = Container(
    length=10,
    width=10,
    height=10
)

milp_algorithm = MILPAlgorithm(
    container=milp_container,
    boxes=boxes
)

(
    milp_packed_boxes,
    milp_unpacked_boxes,
    milp_placements
) = milp_algorithm.solve()

milp_packed_volume = sum(
    box.volume()
    for box in milp_packed_boxes
)

plot_packing(
    milp_container,
    milp_placements,
    "MILP 3D Packing Solution (60 s Time Limit)",
    milp_packed_volume,
    len(boxes),
    "results/milp_20_boxes_packing.png"
)


# --------------------------------------------------
# GENETIC ALGORITHM
# --------------------------------------------------

ga_container = Container(
    length=10,
    width=10,
    height=10
)

ga_algorithm = GeneticAlgorithm(
    container=ga_container,
    boxes=boxes,
    population_size=20,
    generations=50,
    mutation_rate=0.1
)

(
    best_chromosome,
    ga_best_fitness,
    ga_packed_boxes,
    ga_unpacked_boxes,
    ga_placements
) = ga_algorithm.run()

plot_packing(
    ga_container,
    ga_placements,
    "Genetic Algorithm 3D Packing Solution",
    ga_best_fitness,
    len(boxes),
    "results/ga_20_boxes_packing.png"
)


print("3D packing visualisations saved successfully.")