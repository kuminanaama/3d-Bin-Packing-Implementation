from src.models.placement import Placement
from src.models.extreme_point import ExtremePoint

def generate_extreme_points(placement: Placement) -> list[ExtremePoint]:
    """
    Generate extreme points based on the placement of a box in the container.
    
    Args:
        placement (Placement): The placement of the box in the container.
        
    Returns:
        list[ExtremePoint]: A list of extreme points generated from the placement.
    """
    extreme_points = []
    
    # Generate extreme points based on the placement's coordinates and dimensions
    extreme_points.append(ExtremePoint(placement.x + placement.placed_length, placement.y, placement.z))

    extreme_points.append(ExtremePoint(placement.x, placement.y + placement.placed_width, placement.z))

    extreme_points.append(ExtremePoint(placement.x, placement.y, placement.z + placement.placed_height))
    
    return extreme_points