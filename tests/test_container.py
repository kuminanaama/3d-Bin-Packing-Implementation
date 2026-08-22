from src.models.container import Container

container = Container(10.0, 10.0, 10.0)

print(f"Dimensions: {container.length} x {container.width} x {container.height}")

print(f"Volume: {container.volume()}")

print(f"Placements: {container.placements}")