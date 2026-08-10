from src.models.placement import Placement


def collides(a: Placement, b: Placement) -> bool:
    """
    Check if the given placements collide with each other.

    Args:
        a (Placement): The first placement to check.
        b (Placement): The second placement to check.

    Returns:
        bool: True if the placements collide, False otherwise.
    """
    # Check if the placements overlap
    if (a.x < b.x + b.placed_length and
        a.x + a.placed_length > b.x and
        a.y < b.y + b.placed_width and
        a.y + a.placed_width > b.y and
        a.z < b.z + b.placed_height and
        a.z + a.placed_height > b.z):
        return True
    return False
   
