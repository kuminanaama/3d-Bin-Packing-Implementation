from src.models.box import Box
from src.models.placement import Placement
from src.utils.collision_checker import collides

box1 = Box("B1", length=4, width=4, height=4)
box2 = Box("B2", length=2, width=2, height=2)

#Test 1 = Actual collision
placement1 = Placement(box1, x=0, y=0, z=0, placed_length=4, placed_width=4, placed_height=4)

placement2 = Placement(box2, x=1, y=1, z=1, placed_length=2, placed_width=2, placed_height=2)

collision = collides(placement1, placement2)

print(f"Collision detected: {collision}")

#Test 2 = No collision(Far Apart)

placement3 = Placement(box2, x=5, y=5, z=5, placed_length=2, placed_width=2, placed_height=2)

collision2 = collides(placement1, placement3)

print(f"Collision detected: {collision2}")

#Test 3 = No collision(Adjacent, ie.they touch but do not overlap)

placement4 = Placement(box2, x=4, y=4, z=4, placed_length=2, placed_width=2, placed_height=2)

collision3 = collides(placement1, placement4)

print(f"Collision detected: {collision3}")

#Test 4 = No collision(seperated by a gap ie.on the z axis)

placement5 = Placement(box2, x=1, y=1, z=5, placed_length=2, placed_width=2, placed_height=2)

collision4 = collides(placement1, placement5)

print(f"Collision detected: {collision4}")






