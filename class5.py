"""number = 5
if number>0:
    print("positive number")"""

cost= float(input(" please enter the actual product price:")) 
sale = float(input("please enter the sales amount: "))
if (sale > cost):
    amount = sale - cost
    print("total profit = {0}".format(amount))
else:
    print("no profit!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")