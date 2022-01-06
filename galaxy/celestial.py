class Dimension:
    def __init__(self, x, y, z):
        self.x_axis = x
        self.y_axis = y
        self.z_axis = z


class Celestial:
    def __init__(self, diameter, distance):
        self.diameter = diameter
        self.distance = distance


if __name__ == "__main__":
    sun = Celestial(1391000, 0)
    print(sun.distance, sun.diameter)
