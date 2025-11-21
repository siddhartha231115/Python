age_input = input("enter your age: ")
if not age_input.isdigit():
    print("error: age must be a positive number.")
else:
    age = int(age_input)
    if age < 0 or age > 130:
        print("error: enter a realistic age.")
    else:
        print("age is valid.")
        if age % 2 == 0:
            print("the age is even.")
        else:
            print("the age is odd.")