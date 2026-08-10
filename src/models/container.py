from src.models.placement import Placement
from src.utils.boundary_checker import fits_inside  
from src.utils.collision_checker import collides

class Container:
    def __init__(self, length: float, width: float, height: float):
        
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Container dimensions must be greater than zero")

        self.length = length
        self.width = width
        self.height = height
        self.placements = []

    def volume(self) -> float:
        return self.length * self.width * self.height


    def can_place(self, placement: Placement) -> bool:
        if not fits_inside(self, placement):
            return False

        for existing_placement in self.placements:
            if collides(existing_placement, placement):
                return False

        return True

    def add_placement(self, placement: Placement) -> bool:
        if self.can_place(placement):
            self.placements.append(placement)
            return True
        return False

