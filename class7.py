"""medical = input("did you have a medical cause Y or N:")
attendence = int(input("enter the attendence of the student:"))
if medical == 'Y':
    print("you are allowed")
else:
    if attendence>=75:
        print("allowed")
    else:
        print("not allowed")"""

units = int(input("please enter number of units you consumed:"))
if(units < 50):
    amount=units*2.60
    surcharge = 25
elif(units <= 100):
    amount = 130 + ((units - 50)*3.25)
    surcharge = 35
elif(units <= 200):
    amount = 130  + 162.50  + ((units - 100)*5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200)*8.45)
    surcharge = 75
total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total)