from src .models.box import Box
from src.models.placement import Placement

box = Box(box_id="box1", length=2.0, width=3.0, height=4.0)

placement = Placement(box=box, x=1.0, y=2.0, z=3.0, placed_length=2.0, placed_width=3.0, placed_height=4.0)

print(f"Box ID: {placement.box.box_id}")
print(f"Placement Coordinates: ({placement.x}, {placement.y}, {placement.z})")
print(f"Placed Dimensions: {placement.placed_length} x {placement.placed_width} x {placement.placed_height}")