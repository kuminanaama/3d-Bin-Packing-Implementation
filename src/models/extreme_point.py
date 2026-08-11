class ExtremePoint:
    def __init__(self, x: float, y: float, z: float):

        if x < 0 or y < 0 or z < 0:
            raise ValueError("Extreme point coordinates must be non-negative")

        self.x = x
        self.y = y
        self.z = z

        