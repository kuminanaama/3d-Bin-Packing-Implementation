from src.models.box import Box

class Placement:
    def __init__(
            self,
            box: Box, 
            x: float,
            y: float,
            z: float,
            placed_length: float,
            placed_width: float,
            placed_height: float):
        
        if x < 0 or y < 0 or z < 0:
            raise ValueError("Placement coordinates must be non-negative")

        if placed_length <= 0 or placed_width <= 0 or placed_height <= 0 :
            raise ValueError("Placed dimensions must be greater than zero")

        if (placed_length, placed_width, placed_height) not in box.orientations():
            raise ValueError("Placed dimensions must match one of the box's orientations")

        self.box = box
        self.x = x  
        self.y = y
        self.z = z
        self.placed_length = placed_length
        self.placed_width = placed_width
        self.placed_height = placed_height
