class Container:
    def __init__(self, length: float, width: float, height: float):
        
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Container dimensions must be greater than zero")

        self.length = length
        self.width = width
        self.height = height
        self.placed_boxes = []

    def volume(self) -> float:
        return self.length * self.width * self.height

