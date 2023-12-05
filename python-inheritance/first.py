class Human:
  def eat(self):
    print("I can eat")
  def work(self):
    print("I can work")

class Male():
  def flirt(self):
    print("I can flirt")
  def work(self):
    print("I can code")

class Boy(Human, Male):
  pass

# First object of our inheritance class Boy
boy_1 = Boy()

# calling the first method here
boy_1.flirt()

# obtainig method work() from the class Male without
# printing one in Human class by default
boy_1.work()

# How to see how method are arranged in order
print(Boy.mro())