class Circle:
  def __init__(self, radius):
    self.__radius = radius

  @property
  def radius(self):
    return self.__radius
  
  @radius.setter
  def radius(self, value):

    if isinstance (value, int):
      raise TypeError("Value should be an int")
    elif value < 0:
      raise ValueError("Value should be positive")
    self.__radius = value

# Testing the getters and setters of the circle object
circle1 = Circle("hey")
print(circle1.radius)

#Trying to print with negative then printing the initial value
circle2 = Circle(-1)
try:
  circle2.radius = -4
except Exception as e:
  print(e)
finally:
  print(circle2.radius)

#Testing for non-integer values
try:
  circle1.radius = "hello"
except Exception as e:
  print(e)
finally:
  print(circle1.radius)


# try:
#   circle2.radius = 7
# except Exception as e:
#   print ("Error occurred while setting a negative or non-integer value for radius", str(e))
# else:
#   print("Radius successfully updated to ", circle2.radius)