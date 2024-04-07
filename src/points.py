"""
Classes defining playing field and points given in the gaming code test.
"""


class PlayingField:
    def __init__(self):
        self.points = []
    
    def add_point(self, point: object):
        self.points.append(point)


class Point:
    def __init__(self, playing_field: PlayingField, position: tuple, direction: str, id: int = None):
        self.playing_field = playing_field
        self.id = id if id else -1
        self.position = position
        self.direction = self._get_vector_direction(direction)

    def _get_vector_direction(self, direction):
        if direction == "North":
            return (0, 1)
        elif direction == "East":
            return (1, 0)
        elif direction == "South":
            return (0, -1)
        elif direction == "West":
            return (-1, 0)
        else:
            raise ValueError("direction must be one of North, East, South, West.")
        
    def get_points_in_range(self):
        points_in_range = []
        for point in self.playing_field.points:
            if point.id != self.id and self.in_cone(point):
                points_in_range.append(point)
        
    def in_cone(point):
        """
        Function which checks if `point` is inside the cone of the current point.
        """
        return NotImplementedError("Need to implement this.")
    