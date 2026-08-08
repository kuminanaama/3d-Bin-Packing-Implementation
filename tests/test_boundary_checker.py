from src.models.container import Container
from src.models.box import Box
from src.models.placement import Placement
from src.utils.boundary_checker import fits_inside  

container = Container(length=10.0, width=10.0, height=10.0)

box = Box(box_id="box1", length=2.0, width=3.0, height=4.0)

placement1 = Placement(box=box, x=1.0, y=2.0, z=3.0, placed_length=2.0, placed_width=3.0, placed_height=4.0)

print(f"Placement 1 fits inside container: {fits_inside(container, placement1)}")

placement2 = Placement(box=box, x=6.0, y=7.0, z=8.0, placed_length=4.0, placed_width=3.0, placed_height=2.0)

print(f"Placement 2 fits inside container: {fits_inside(container, placement2)}")

placement3 = Placement(box=box, x=7.0, y=2.0, z=2.0, placed_length=4.0, placed_width=3.0, placed_height=2.0)

print(f"Placement 3 fits inside container: {fits_inside(container, placement3)}")