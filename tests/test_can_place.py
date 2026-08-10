from src.models.box import Box
from src.models.placement import Placement
from src.models.container import Container

container = Container(length=10, width=10, height=10)

box1 = Box("B1", length=4, width=4, height=4)
box2 = Box("B2", length=2, width=2, height=2)

#Test 1 = fits_inside should return True and no collision should be detected since the container is empty
placement1 = Placement(box1, x=0, y=0, z=0, placed_length=4, placed_width=4, placed_height=4)


print(f"Can place box1 at placement1: {container.can_place(placement1)}")

#Test 2 = fits_inside should return False since the box is outside the container
placement2 = Placement(box1, x=7, y=7, z=7, placed_length=4, placed_width=4, placed_height=4)

print(f"Can place box1 at placement2: {container.can_place(placement2)}")

