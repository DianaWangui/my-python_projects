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
    return 2 * Circle.pi * self.__radius **2
  def circumference_circle(self):
    return 2 * Circle.pi * self.__radius
  
circle_1 = Circle(4)
print(f"Area is: {circle_1.area_circle()}")
#circle_1 = Circle(4)
print(circle_1.circumference_circle())