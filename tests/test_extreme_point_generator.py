from src.models.box import Box
from src.models.placement import Placement
from src.utils.extreme_point_generator import generate_extreme_points

box = Box("box1", 10, 20, 30)

placement = Placement(box, x=0, y=0, z=0, placed_length=10, placed_width=20, placed_height=30)

extreme_points = generate_extreme_points(placement)

for point in extreme_points:
    print(f"Extreme Point: ({point.x}, {point.y}, {point.z})")