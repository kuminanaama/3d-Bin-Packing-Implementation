from src.models.box import Box

box = Box("box1", 2.0, 3.0, 4.0)

print(f"Box ID: {box.box_id}")
print(f"Dimensions: {box.length} x {box.width} x {box.height}")
print(f"Volume: {box.volume()}")
