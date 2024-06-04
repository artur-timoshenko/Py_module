from structures import dot

class triangle:
    def __init__(self, A, B, C):
        if not isinstance(A, dot) or not isinstance(B, dot) or not isinstance(C, dot):
            raise TypeError("Усі точки трикутника повинні бути об'єктами класу Dot")
        self.A = A
        self.B = B
        self.C = C
        self.area = self.calculate_area()

    def calculate_area(self):
        area = 0
        area = 0.5 * abs((self.B.x - self.A.x) * (self.C.y - self.A.y) - (self.C.x - self.A.x) * (self.B.y - self.A.y))
        return area

    def get_area(self):
        return self.area

    def print_points(self):
        print('Трикутник з точками:')
        self.A.print_point()
        self.B.print_point()
        self.C.print_point()