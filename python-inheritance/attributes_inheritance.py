class Human:

  def __init__(self):
    self.nose = 1
    self.eye = 2

  def eat(self):
    print("I can eat")
  def work(self):
    print("I can work")

class Male():
  def __init__(self, name):
    self.name = name

  def flirt(self):
    print("I can flirt")
  def work(self):
    print("I can code")

class Boy(Human, Male):
  def __init__(self, name):
    Male.__init__(self, name)
    Human.__init__(self)

boy_1 = Boy("Dan")
print(boy_1.name)
print(boy_1.nose)
print(boy_1.eye)