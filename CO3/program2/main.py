from graphics import rectangle,circle
from graphics.threedgraphics import *
from graphics.threedgraphics import cuboid
from graphics.threedgraphics import sphere as s

l = int(input("\nEnter length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
print("Area of the given rectangle=", rectangle.area(l, b))
print("Perimeter of the given rectangle=", rectangle.perimeter(l, b))
print("____________________________________________________")

r = int(input("Enter the radius:"))
print("Area of the given circle=", circle.area(r))
print("Perimeter of the given circle=", circle.perimeter(r))
print("____________________________________________________")

l = int(input("\nEnter length of the cuboid:"))
b=int(input("Enter breadth of the cuboid:"))
h=int(input("Enter height of the cuboid:"))
print("Area of the given cuboid=",cuboid.area(1,b,h))
print("Perimeter of the given cuboid=",cuboid.perimeter(l,b,h))
print("____________________________________________________")

r = int(input("\nEnter the radius of the sphere:"))
print("Area of the given sphere=", s.area(r))
print("Perimeter of the given circle=", s.perimeter(r))
print("____________________________________________________")

