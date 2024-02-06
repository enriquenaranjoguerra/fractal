# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from src import fractal as fr
import numpy as np
import matplotlib.pyplot as plt

points = 2
top_level = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y


class Segment:
    def __init__(self, p1: Point, p2: Point):
        if not (isinstance(p1, Point) & isinstance(p2, Point)):
            raise TypeError("No son clase Point")
        self.p1 = p1
        self.p2 = p2

    def get_coordinates(self):
        return [[self.p1.x, self.p1.y], [self.p2.x, self.p2.y]]

    def get_coordinates_x(self):
        return [self.p1.x, self.p2.x]

    def get_coordinates_y(self):
        return [self.p1.y, self.p2.y]

    def __eq__(self, other):
        if isinstance(other, Segment):
            return self.p1 == other.p1 and self.p2 == other.p2

    def __str__(self):
        return f"Seg([{self.p1.x}, {self.p1.y}], [{self.p2.x}, {self.p2.y}])"


class Draw:
    def __init__(self, basis, segments):
        self.basis = basis
        self.segments = segments

    def __str__(self):
        return f"{self.basis}, {self.segments}"


def get_circumference(center, radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    return [center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta)]


def generate_segment(base: Point, direction, scale=1.0):
    """
    This function creates a segments from a base point, a direction and a scale.

    :param base: the centre point.
    :param direction: the direction vector.
    :param scale: the redimension parameter.
    :return: returns a Segments.
    """
    first_point = [base.x - direction[0], base.y - direction[1]]
    final_point = [base.x + direction[0], base.y + direction[1]]

    p1 = Point(scale * first_point[0], scale * first_point[1])
    p2 = Point(scale * final_point[0], scale * final_point[1])

    return Segment(p1, p2)


def get_color_by_level(lev):
    if lev == 0:
        return 'black'
    else:
        if lev == 1:
            return 'blue'
    return 'red'


def generate_main_draw(base, ang, scale=1.0, rotation=0.0):
    """
    This function creates some segments from a base point, some angles, a scale and a rotation.

    :param base: the centre point.
    :param ang: the segments angle.
    :param scale: the redimension parameter.
    :param rotation: the rotation parameter.
    :return: returns an array of Segments.
    """
    segments = []
    new_basis = []

    for a in range(len(ang)):
        dir = [np.cos(ang[a] + rotation), np.sin(ang[a] + rotation)]
        new_segment = generate_segment(base, dir, scale * 1 / np.power(2, a + 1))
        segments.append(new_segment)
        new_basis.append(Point(new_segment.p1.x, new_segment.p1.y))
        new_basis.append(Point(new_segment.p2.x, new_segment.p2.y))
    return Draw(new_basis, segments)


if __name__ == '__main__':
    circumference = get_circumference([0, 0], 1)
    plt.plot(circumference[0], circumference[1])

    angles = []

    for i in range(points):
        angles.append(1 - 1 / (i + 1))

    angles = np.array(angles) * np.pi

    # angles = np.random.rand(4) * np.pi
    # angles = sorted(angles)

    basis = [Point(0, 0)]
    segments = []

    for i in range(top_level):
        new_basis = []
        for b in basis:
            draw = generate_main_draw(b, angles, float(1 / (i + 1)), i * np.pi * 0.25)
            segments.append(draw.segments)
            new_basis.extend(draw.basis)
        basis = new_basis

    for seg in segments:
        for s in seg:
            plt.plot(s.get_coordinates_x(), s.get_coordinates_y(), linestyle='-', color='black')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
