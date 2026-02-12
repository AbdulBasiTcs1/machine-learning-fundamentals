class Trapezoid:
    
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * (self.a + self.b) * self.h



class Parallelogram:
    
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height


class ShapeComparison:
    def __init__(self):
        self.results = {}

    def add_shape(self, name, area):
        self.results[name] = area

    def find_largest(self):
        largest_shape = max(self.results, key=self.results.get)
        return largest_shape, self.results[largest_shape]

    def display_all(self):
        for shape, area in self.results.items():
            print(f"{shape} Area = {area}")


comparison = ShapeComparison()

t1 = Trapezoid(4, 6, 5)
t2 = Trapezoid(3, 7, 4)

p1 = Parallelogram(5, 6)
p2 = Parallelogram(8, 3)

comparison.add_shape("Trapezoid1", t1.area())
comparison.add_shape("Trapezoid2", t2.area())
comparison.add_shape("Parallelogram1", p1.area())
comparison.add_shape("Parallelogram2", p2.area())

print("All Shape Areas:")
comparison.display_all()

largest_shape, largest_area = comparison.find_largest()

print("\nShape with Largest Area:")
print(f"{largest_shape} with area = {largest_area}")
