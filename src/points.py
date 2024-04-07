"""
Classes defining playing field and points given in the gaming code test.
"""
import numpy as np
import math


def theta(x, y):
    """
    Finds angle theta in degrees of a point, relative to the origin (0, 0).
    https://en.wikipedia.org/wiki/Euler%27s_formula
    https://www.cuemath.com/trigonometry/arctan/

    Returns a number of degrees between -180 and 180
    """
    return math.atan2(y, x)/math.pi*180

class PlayingField:
    def __init__(self):
        self.points = []
    
    def add_point(self, point: object):
        self.points.append(point)

    def visible_points(self, id, angle_degrees, distance):
        """
        Fetch all points in the playing field which are within the cone
        of point corresponding to `id`.
        """
        # first find the point in the playing field corresponding to `id`
        points = [x for x in self.points if x.id == id]
        if len(points) > 1:
            raise ValueError(f"Non-unique identifier: {id}")
        point = points[0]

        # now find the points inside the cone of point
        visible_points = []
        for other_point in self.points:
            if other_point.id == point.id:
                continue
            if point.in_cone(other_point, angle_degrees, distance):
                visible_points.append(other_point)

        print(
            f"Points in the visible range of {point.id}: " +
            f"{[x.id for x in visible_points]}"
        )

        return visible_points


class Point:
    def __init__(self, playing_field: PlayingField, position: tuple, direction: str, id: int = None):
        self.playing_field = playing_field
        self.id = id if id else -1
        self.position = np.array(position)
        self.direction = self._get_vector_direction(direction)

    def _get_vector_direction(self, direction):
        if direction == "North":
            return np.array([0, 1])
        elif direction == "East":
            return np.array([1, 0])
        elif direction == "South":
            return np.array([0, -1])
        elif direction == "West":
            return np.array([-1, 0])
        else:
            raise ValueError("direction must be one of North, East, South, West.")
        
    def get_points_in_range(self):
        points_in_range = []
        for point in self.playing_field.points:
            if point.id != self.id and self.in_cone(point):
                points_in_range.append(point)
        
    def in_cone(self, point, angle_degrees, distance):
        """
        Function which checks if `point` is inside the cone of the current point.
        """
        # 1. check if distance between self and point is greater than distance
        dist = np.linalg.norm(self.position - point.position)
        if dist > distance:
            return False

        # 2. check if relative direction of point to self is within angle/2 from the
        #    direction self is pointing in
        # https://en.wikipedia.org/wiki/Euler%27s_formula
        relative_direction = point.position - self.position
        relative_angle = theta(relative_direction[0], relative_direction[1]) % 360

        # get the angle of the upper and lower bounds of circle segmemt / cone
        upper_direction_angle = (theta(self.direction[0], self.direction[1]) + angle_degrees) % 360
        lower_direction_angle = (theta(self.direction[0], self.direction[1]) - angle_degrees) % 360

        # check if the direction is outside of the cone
        if relative_angle > upper_direction_angle or relative_angle < lower_direction_angle:
            return False

        # 3. If distance is short enough, and the direction is inside the cone, then we
        #    conclude that `point` is inside the cone of `self`
        return True
    