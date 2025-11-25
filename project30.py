n = int(input("enter a number: "))
odd_numbers = [i for i in range(1, n) if i % 2 != 0]
print("odd numbers under", n, ":", odd_numbers)
numbers = [3, 4, 7, 8, 11, 12, 15]
odd_list = [x for x in numbers if x % 2 != 0]
print("odd numbers from list:", odd_list)
fruits = ["apple", "banana", "mango", "orange"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("updated fruits:", capitalized_fruits)