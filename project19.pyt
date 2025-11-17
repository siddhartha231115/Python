t=int(input("enter start range: "))
d=int(input("enter end range: "))

even_squares=[]
odd_squares=[]

for num in range(t,d+1):
    sq=num*num
    if sq %2==0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

print("even squares:", even_squares)
print("odd squares:", odd_squares)