def add(a, b):
  c = a + b
  return c

def sub(a, b):
  sub = a - b
  return sub

def mul(a, b):
  mul = a * b
  return mul

def div(a, b):
  div = a / b
  return div


def simple_cal():
  first = int(input("Enter your first value: "))
  print("Operators:\n+\n-\n*\n/\n")

  operator = input("Chose the operator: ")
  second = int(input("Enter your second value: "))
  if operator == '+':
    print(add(first, second))
  elif operator == '-':
    print(sub(first, second))
  elif operator == '*':
    print(mul(first, second))
  else:
    print(div(first, second))
  
  while True:
    try:
      choice = input("Enter 'y' to continue or 'n' to quit: ")
      if choice.lower() == 'y':
        simple_cal()
      elif choice.lower() == 'n':
        exit()
        #break
    except Exception as e:
      print(e)
      #continue


simple_cal()
    # try:
    #   result = operator(first,second)
    #   break
    # except ZeroDivisionError as e:
    #   print ("You can't divide by zero! Try again.")
    #   continue
    # except Exception as e:
    #   print ("An error occurred. Please try again.")
    #   continue
    # finally:
    #   print ("The final answer is",result)