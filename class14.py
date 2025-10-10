"""def total_calc(bill_amount,tip_perc):
    total = bill_amount*(1+ 0.01*tip_perc)
    print(f"please pay ${total}")
total_calc(5000,10)"""

"""def cube(number):
    return number*number*number
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))"""

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))