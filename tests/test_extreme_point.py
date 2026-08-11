from src.models.extreme_point import ExtremePoint

extreme_point = ExtremePoint(1, 2, 3)

print(f"Extreme Point Coordinates: x={extreme_point.x}, y={extreme_point.y}, z={extreme_point.z}")

#This will raise a ValueError because the x coordinate is negative
extreme_point_negative = ExtremePoint(-1, 2, 3)  # This will raise a ValueError


