"""def wel_wishes():
    print("hello")
    print("how are you")

wel_wishes()"""

"""summer="hot"
winter="cold"
def weather_condition():
    print("the weather in the summer is ",summer)
    print("the weather in the winter is ",winter)
weather_condition()  """

def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply (P,Q):
    return P * Q
def divide(P,Q):
    return P / Q
print("Please select the Operater")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Please enter choice (a/b/c/d/):")
numone = int(input("Please enter the first number:"))
numtwo = int(input("Please enter the second number:"))
if choice == "a":
    print(add(numone,numtwo))
elif choice == "b":
    print(subtract(numone,numtwo))
elif choice == "c":
    print(multiply(numone,numtwo))
elif choice == "d":
    print(divide(numone,numtwo))
else:
    print("this is an invalid input")