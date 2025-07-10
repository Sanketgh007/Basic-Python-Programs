from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self):
        self.area = 0.0

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def calculate(self):
        pass

    def display(self):
        print(f"The area is: {self.area}")

class Circle(Shapes):
    def __init__(self):
        super().__init__()
        self.pi = 3.14678
        self.r = 0.0

    def collect(self):
        self.r = float(input("Enter the radius: "))

    def calculate(self):
        self.area = self.pi * self.r * self.r

class Rectangle(Shapes):
    def __init__(self):
        super().__init__()
        self.l = 0.0
        self.b = 0.0

    def collect(self):
        self.l = float(input("Enter the value of length: "))
        self.b = float(input("Enter the value of breadth: "))

    def calculate(self):
        self.area = self.l * self.b

class Square(Shapes):
    def __init__(self):
        super().__init__()
        self.side = 0.0

    def collect(self):
        self.side = float(input("Enter the value of side: "))

    def calculate(self):
        self.area = self.side * self.side

class Geometry:
    def permit(self, shape: Shapes):
        shape.collect()
        shape.calculate()
        shape.display()

if __name__ == "__main__":
    g = Geometry()
    c = Circle()
    s = Square()
    r = Rectangle()

    g.permit(c)
    print("--------------------------------")
    g.permit(s)
    print("--------------------------------")
    g.permit(r)
    print("--------------------------------")
