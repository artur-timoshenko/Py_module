from abc import abstractmethod
import math
from structures import dot,angle,line
from triangle import triangle

@abstractmethod
class quadrangle:
#тип фігури
    figure_type = "Чотирикутник"
#вершини
    a = dot(0,0)
    b = dot(0,0)
    c = dot(0,0)
    d = dot(0,0)
#довжини сторін
    AB_length = 0
    BC_length = 0
    CD_length = 0
    DA_length = 0
#кути
    angleB = 0
    angleC = 0
    angleD = 0
    angleA = 0
#стоорони 
    lineAB = line(a,b)
    lineBC = line(b,c)
    lineCD = line(c,d)
    lineDA = line(d,a)
#діагоналі
    diagonalAC = 0
    diagonalDB = 0
#периметр й площа
    perimeter = 0
    area = 0

    def __init__(self, a, b, c, d):
        if not isinstance(a, dot) or not isinstance(b, dot) or not isinstance(c, dot) or not isinstance(d, dot):
            raise TypeError("Усі точки чотирикутника повинні бути об'єктами класу dot")
    
        if self.calculate_sum_of_angles(a, b, c, d) != 360:
            raise ValueError("Фігура з цими точками не є опуклим чотирикутником,сума кутів не 360")

        if self.do_diagonals_intersect(a, b, c, d):
            raise ValueError("Фігура з цими точками не є опуклим чотирикутником,діагоналі перетинаються")

        self.figure_type = "Чотирикутник"
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.set_angles()
        self.set_sides()
        self.set_sides_length()
        self.set_perimeter()
        self.set_area()
        self.set_diagonales_length()

    def set_perimeter(self):
        self.perimeter = self.AB_length + self.BC_length + self.CD_length + self.DA_length

    def set_area(self):
        self.area = self.calculate_area()

    def set_angles(self):
        self.angleB = angle(self.a, self.b, self.c).degrees
        self.angleC = angle(self.b, self.c, self.d).degrees
        self.angleD = angle(self.c, self.d, self.a).degrees
        self.angleA = angle(self.d, self.a, self.b).degrees

    def set_sides(self):
        self.lineAB = line(self.a,self.b)
        self.lineBC = line(self.b,self.c)
        self.lineCD = line(self.c,self.d)
        self.lineDA = line(self.d,self.a)

    def set_sides_length(self):
        self.AB_length = self.lineAB.length()
        self.BC_length = self.lineBC.length()
        self.CD_length = self.lineCD.length()
        self.DA_length = self.lineDA.length()

    def set_diagonales_length(self):
        self.diagonalAC = line(self.a,self.c).length()
        self.diagonalDB = line(self.b,self.d).length()
    def calculate_sum_of_angles(self, a, b, c, d):
        sum_of_angles = angle(a, b, c).degrees + angle(b, c, d).degrees + angle(c, d, a).degrees + angle(d, a, b).degrees
        if(sum_of_angles < 360.5 and sum_of_angles > 359.5):
            return 360
        else:
            return math.floor(sum_of_angles)

    def do_diagonals_intersect(self, a, b, c, d):
        def on_segment(p, q, r):
            """Функція, яка перевіряє, чи точка q лежить на відрізку pr."""
            if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
                q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
                return True
            return False

        def orientation(p, q, r):
            """Функція, яка повертає орієнтацію векторного добутку між відрізками pq та pr."""
            val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
            if val == 0:
                return 0  # Колінеарні
            elif val > 0:
                return 1  # За годинниковою стрілкою
            else:
                return 2  # Проти годинникової стрілки

        # Отримати орієнтації для кожної точки
        o1 = orientation(a, b, c)
        o2 = orientation(a, b, d)
        o3 = orientation(c, d, a)
        o4 = orientation(c, d, b)

        # Перевірка на перетин діагоналей
        if (o1 != o2 and o3 != o4):
            return True

        # Якщо вершини лежать на одній прямій
        if (o1 == 0 and on_segment(a, c, b)):
            return True
        if (o2 == 0 and on_segment(a, d, b)):
            return True
        if (o3 == 0 and on_segment(c, a, d)):
            return True
        if (o4 == 0 and on_segment(c, b, d)):
            return True

        return False
        
    def calculate_area(self):
        triangle1 = triangle(self.a, self.b, self.c)
        triangle2 = triangle(self.a, self.c, self.d)
        total_area = triangle1.get_area() + triangle2.get_area()
        return total_area
    

    def print_points(self):
        print(self.figure_type , 'з точками:')
        self.a.print_point()
        self.b.print_point()
        self.c.print_point()
        self.d.print_point()

    def print_allInfo(self):
        print("Тип фігури:", self.figure_type)
        print("Вершина A:", self.a.print_point())
        print("Вершина B:", self.b.print_point())
        print("Вершина C:", self.c.print_point())
        print("Вершина D:", self.d.print_point())
        print("Довжина сторони AB:", round(self.AB_length, 2))
        print("Довжина сторони BC:", round(self.BC_length, 2))
        print("Довжина сторони CD:", round(self.CD_length, 2))
        print("Довжина сторони DA:", round(self.DA_length, 2))
        print("Довжина діагоналі AC:", round(self.diagonalAC, 2))
        print("Довжина сторони DB:", round(self.diagonalDB, 2))
        print("Кут B:", round(self.angleB, 2))
        print("Кут C:", round(self.angleC, 2))
        print("Кут D:", round(self.angleD, 2))
        print("Кут A:", round(self.angleA, 2))
        print("Периметр:", round(self.perimeter, 2))
        print("Площа:", round(self.area, 2))
    
    def compare_by_area(self, other):
        if(self.area > other.area):
            print("Фігура більша по площі за іншу фігуру")
        elif(self.area == other.area):
            print("Фігури рівні")
        else:
            print("Фігура менша по площі за іншу фігуру")

    def compare_by_perimeter(self, other):
        if(self.perimeter > other.perimeter):
            print("Фігура більша по периметру за іншу фігуру")
        elif(self.perimeter == other.perimeter):
            print("Фігури рівні")
        else:
            print("Фігура менша по периметру за іншу фігуру")

    def compare_by_perimeterAndArea(self, other):
        self.compare_by_area(other)
        self.compare_by_perimeter(other)

    
    def get_subtypes(self):
        return ["Чотирикутник"]