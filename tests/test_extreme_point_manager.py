from src.models.box import Box
from src.models.placement import Placement
from src.models.extreme_point import ExtremePoint
from src.utils.extreme_point_manager import ExtremePointManager


manager = ExtremePointManager()

print("Initial points:")
for point in manager.extreme_points:
    print(point.x, point.y, point.z)


box = Box("B1", 4, 3, 2)

placement = Placement(
    box=box,
    x=0,
    y=0,
    z=0,
    placed_length=4,
    placed_width=3,
    placed_height=2
)

used_point = ExtremePoint(0, 0, 0)
manager.update_extreme_points(used_point, placement)

print("\nAfter updating extreme points:")
for point in manager.extreme_points:
    print(point.x, point.y, point.z)