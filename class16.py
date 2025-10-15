"""try:
    number = int(input("Enter a number"))
    print("The number entered is",number)
except ValueError as ex:
    print("Exception:",ex)"""

"""try:
    num1, num2 = eval(input("enter two numbers,, seperated by a comma"))
    result = num1 / num2
    print("result is",result)
except ZeroDivisionError:
    print("Division by zero is error!!!!!!!!!!!!!!!!!!!!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like thi 1,2")
except:
    print("Wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")"""

valid = False
while not valid:
    try:
        n=int(input("enter a number"))
        while n%2==0:
            print("bye")
        valid = True
    except ValueError:
        print("Invalid")