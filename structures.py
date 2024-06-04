import math

class dot:
    def  __init__(self, x,y):
        self.x = x
        self.y = y

    def print_point(self):
        print('(', self.x , ',', self.y, ')')
        
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class angle:
    figure_type = "кут"
    degrees = 0
    a1 = dot(0,0)
    a2 = dot(0,0)
    a3 = dot(0,0)
    def __init__(self,a1,a2,a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.set_degrees()
        self.set_figure_type_by_degrees()

    def set_degrees(self):
        vector_AB = (self.a2.x - self.a1.x, self.a2.y - self.a1.y)
        vector_BC = (self.a3.x - self.a2.x, self.a3.y - self.a2.y)

        dot_product = vector_AB[0] * vector_BC[0] + vector_AB[1] * vector_BC[1]
        
        # Обчислення довжин векторів AB і BC
        length_AB = math.sqrt((self.a2.x - self.a1.x)**2 + (self.a2.y - self.a1.y)**2)
        length_BC = math.sqrt((self.a3.x - self.a2.x)**2 + (self.a3.y - self.a2.y)**2)
        
        cos_angle = dot_product / (length_AB * length_BC)
        
        self.degrees = 180 - round(math.degrees(math.acos(cos_angle)),2)

    def set_figure_type_by_degrees(self):
        if self.degrees < 90:
            self.figure_type = "Гострий кут"
        elif self.degrees == 90:
            self.figure_type = "Прямий кут"
        else:
            self.figure_type = "Тупий кут"
    
    def print_points(self):
        print(self.figure_type , 'з точками:')
        self.a1.print_point()
        self.a2.print_point()
        self.a3.print_point()
        print(self.degrees, " градусів")

class line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        """Обчислює довжину відрізка."""
        return ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) ** 0.5