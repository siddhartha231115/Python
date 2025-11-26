class IntegerToRoman:
    def __init__(self, number):
        self.number = number
    def convert(self):
        roman_values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        num = self.number
        result = ""
        for value, symbol in roman_values:
            while num >= value:
                result += symbol
                num -= value
        return result
if __name__ == "__main__":
    number1 = IntegerToRoman(29)
    print("29  ->", number1.convert())
    number2 = IntegerToRoman(944)
    print("944 ->", number2.convert())
    number3 = IntegerToRoman(2025)
    print("2025 ->", number3.convert())
