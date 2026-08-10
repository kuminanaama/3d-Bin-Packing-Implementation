from src.models.box import Box
from src.models.placement import Placement
from src.models.container import Container

container = Container(length=10, width=10, height=10)

box1 = Box("B1", length=4, width=4, height=4)
box2 = Box("B2", length=2, width=2, height=2)

#Test 1 = Add a placement that fits inside the container and does not collide with any existing placements
placement1 = Placement(box=box1, x=0, y=0, z=0, placed_length= 4, placed_width= 4, placed_height= 4)

print("Adding placement 1:", container.add_placement(placement1))  # Expected: True

#Test 2 = Placement that fits inside the container but collides with an existing placement , therefore should not be added
placement2 = Placement(box=box2, x=3, y=3, z=3, placed_length= 2, placed_width= 2, placed_height= 2)

print("Adding placement 2:", container.add_placement(placement2))  # Expected: False

#Test 3 = Add a placement that fits inside the container and does not collide with any existing placements
placement3 = Placement(box=box2, x=5, y=5, z=5, placed_length= 2, placed_width= 2, placed_height= 2)

print("Adding placement 3:", container.add_placement(placement3))  # Expected: True

print ("Total placements in container:", len(container.placements))  # Expected: 2
    