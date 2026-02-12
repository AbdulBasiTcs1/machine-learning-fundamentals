class Shape:
    def area(self):
        raise NotImplementedError


class Trapezoid(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * (self.a + self.b) * self.h


class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class ShapeComparison:
    def __init__(self):
        self.results = {}

    def add_shape(self, name, shape):
        self.results[name] = shape.area()

    def display_all(self):
        for name, area in self.results.items():
            print(f"{name} : Area = {area}")

    def find_largest(self):
        largest = max(self.results, key=self.results.get)
        return largest, self.results[largest]


shapes = {
    "Trapezoid1": Trapezoid(4, 6, 5),
    "Trapezoid2": Trapezoid(3, 7, 4),
    "Parallelogram1": Parallelogram(5, 6),
    "Parallelogram2": Parallelogram(8, 3)
}

comparison = ShapeComparison()

for name, shape in shapes.items():
    comparison.add_shape(name, shape)

comparison.display_all()

largest_shape, largest_area = comparison.find_largest()

print("\nLargest Shape:")
print(f"{largest_shape} -> Area = {largest_area}")
