from structures import dot,angle 
from triangle import triangle
from quadrangle import quadrangle 
from rectangle import rectangle
from squere import square
from rhomb import rhomb
from trapezoid import trapezoid
from rectangular_trapezoid import rectangular_trapezoid

a1 = dot(0,0)
a2 = dot(3,3)
a3 = dot(3,0)
a4 = dot(0,3)
a5 = dot(0,5)
a6 = dot(5,5)
a7 = dot(2,3)
a8 = dot(5,0)
square1 = square(a1, a4, a2, a3)
rhomb1 = rhomb(a1, a4, a2, a3)
rectangle1 = rectangle(a1, a7, a2, a8)
trapezoid1 = trapezoid(a1, a7, a2, a8)
rectangular_trapezoid1 = rectangular_trapezoid(a1, a4, a2, a8)

figures_list = []
figures_list.append(rhomb1)
figures_list.append(rectangle1)
figures_list.append(square1)
figures_list.append(trapezoid1)
figures_list.append(rectangular_trapezoid1)

for figure in figures_list:
    figure.print_allInfo()

rhomb1.compare_by_area(rectangle1)
rhomb1.compare_by_perimeter(rectangle1)
print('\n')
trapezoid1.compare_by_perimeterAndArea(rectangular_trapezoid1)

print('\n')

print(rhomb1.get_subtypes())
print(square1.get_subtypes())
print(rectangle1.get_subtypes())
print(trapezoid1.get_subtypes())
print(rectangular_trapezoid1.get_subtypes())

