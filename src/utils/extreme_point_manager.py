from src.models.placement import Placement
from src.utils.extreme_point_generator import generate_extreme_points
from src.models.extreme_point import ExtremePoint

class ExtremePointManager:
    def __init__(self):
        self.extreme_points = [ExtremePoint(0, 0, 0)]  # Start with the origin as the initial extreme point

    def add_extreme_point(self, extreme_point: ExtremePoint):
        for existing_point in self.extreme_points:
            if (existing_point.x == extreme_point.x and
                existing_point.y == extreme_point.y and
                existing_point.z == extreme_point.z):
                return  # Do not add duplicate extreme points
        self.extreme_points.append(extreme_point)

    def update_extreme_points(self, used_point: ExtremePoint, placement: Placement):
        self.remove_extreme_point(used_point)

        new_extreme_points = generate_extreme_points(placement)

        for point in new_extreme_points:
            self.add_extreme_point(point)

    def remove_extreme_point(self, extreme_point: ExtremePoint):
        for existing_point in self.extreme_points:
            if (existing_point.x == extreme_point.x and
                existing_point.y == extreme_point.y and
                existing_point.z == extreme_point.z):
                self.extreme_points.remove(existing_point)
                return

        

        