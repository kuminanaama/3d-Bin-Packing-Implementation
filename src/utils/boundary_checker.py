from src.models.container import Container
from src.models.placement import Placement

def fits_inside(container,placement):
    if placement.x < 0 or placement.y < 0 or placement.z < 0:
        return False

    if (placement.x + placement.placed_length > container.length or
        placement.y + placement.placed_width > container.width or
        placement.z + placement.placed_height > container.height):
        return False

    return True