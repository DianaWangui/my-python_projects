"""This is a class to find area and perimeter of a circle 
using class and attribute and method instantiations"""

class Circle:
  pi = 3.14
  def __init__(self, radius=0):
    self.__radius = radius

  @property
  def radius(self):
    return self.__radius
  @radius.setter
  def radius(self, value):
    if not isinstance(value, int):
      raise TypeError("Number should be an integer")
    if value <= 0:
      raise ValueError("Value should be greater than zero")
    self.__radius = value
  
  def area_circle(self):
    return Circle.pi * self.__radius **2
  def circumference_circle(self):
    return 2 * Circle.pi * self.__radius
  # Testing the code
if __name__ == "__main__":
  c = Circle()
  print(f'Area of the circle with no radius given is {c.area_circle()}')
  print(f'Circumference of the circle with no radius given is {c.circumference_circle()}')
  c.radius = 5
  print(f'Area of the circle with radius 5 is {c.area_circle()}')
  print(f'Circumference of the circle with radius 5 is {c.circumference_circle()}')


"""A class rectangle to find area and perimeter
of a triangke using properties like getter 
to get the lenght and height and setter
the values"""

# This print is to print an empty line to separate outputs
print()

class Rectangle:
  def __init__(self, length=0, width=0):
    self.__length = length
    self.__width = width
  @property
  def length(self):
    return self.__length
  @length.setter
  def length(self, value):
    if not isinstance(value, int):
      raise TypeError("Length should be an integer")
    if value <= 0:
      raise ValueError("Length should be greater than zero")
    self.__length = value
  @property
  def width(self):
    return self.__width
  @width.setter
  def width(self, value):
    if not isinstance(value, int):
      raise TypeError("Width should be an integer")
    if value <= 0:
      raise ValueError("Width should be greater than zero")
    self.__width = value
  def area_rectangle(self):
    return self.__length * self.__width
  def perimeter_rectangle(self):
    return (self.__length + self.__width) * 2
  
  # Testing the code
if __name__ == "__main__":
  r = Rectangle()
  print(f'Area of the rectangle with no dimensions given is {r.area_rectangle()}')
  print(f'Perimeter of the rectangle with no dimensions given is {r.perimeter_rectangle()}')
  r.length = 4
  r.width = 6
  print(f'Area of the rectangle with length 4 and width 6 is {r.area_rectangle()}')
  print(f'Perimeter of the rectangle with length 4 and width 6 is {r.perimeter_rectangle()}')


"""
Class inheritance to find area and perimeter of a square
using class Rectangle as the parent or super class
"""
#Printing a line to separate outputs
print()
class Square(Rectangle):

  def __init__(self, side=0):
    super().__init__(self, side)
    self.__length = side
  @property
  def side(self):
    return self.__length
  @side.setter
  def side(self, value):
    if not isinstance(value, int):
      raise TypeError("Side should be an integer")
    if value <= 0:
      raise ValueError("Side should be greater than zero")
    self.__length = value
    self.__width = value
  def area_square(self):
    return self.__length ** 2
  def perimeter_square(self):
    return 4 * self.__length
# Testing the code
if __name__ == "__main__":
  s = Square()
  print(f'Area of the square with no dimension given is {s.area_square()}')
  print(f'Perimeter of the square with no dimension given is {s.perimeter_square()}')
  s.side = 5
  print(f'Area of the square with side 5 is {s.area_square()}')
  print(f'Perimeter of the square with side 5 is {s.perimeter_square()}')
