"""a = int(input("enter the value 1:"))
b = int(input("enter the value 2:"))
c = int(input("enter the value 3:"))
d = int(input("enter the value 4:"))
e = int(input("enter the value 5:"))
sum = a+b+c+d+e
print("sum of the values =",sum)
average=sum / 5
print("average =",average)"""

print("enter mark obtained in 5 subjects:")
math = int(input("math:"))
english = int(input("english:"))
science = int(input("science:"))
hindi = int(input("hindi:"))
social = int(input("social:"))
sum = math+english+science+hindi+social
print("sum =",sum)
perc = (sum/500)*100
print(end="Percentage Mark=")
print(perc)