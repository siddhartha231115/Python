"""class IOString():
    def __init__(self):
        self.srt1 = ""
    def get_String(self):
        self.srt1 = input("enter string : ")
    def print_String(self):
        print("result is:",self.srt1.upper())
srt1 = IOString()
srt1.get_String()
srt1.print_String()"""
 
"""class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destuctor called")
def Create_obj():
    print("making object...................................................................................................")
    obj = employee()
    print("function end..................................................................................................")
    return obj
print("calling Create_obj() function.......................................................................................................")
obj = Create_obj()
print("program end.....................................................................................................................................")"""

class pair_elements:
    def twoSum(self,nums,target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num],i)
            lookup[num] = i
value = int(input("enter sum for which you want to make this search"))
print("index1=%d,index2=%d"%
pair_elements().twoSum((10,20,30,40,50,60,70),value))