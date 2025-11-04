"""class student:
    grade = 4
    print("hi i am a student of grade",grade)
object = student()"""

"""class vehicle:
    def __init__(self,max_speed,milage):
        self.max_speed = max_speed
        self.milage = milage
modelx = vehicle(240,18)
print("model max speed:",modelx.max_speed)
print("model milage:",modelx.milage)"""

class parrot:
    species = "bird"
    def __init__(self,name,age,color):
        self.color = color
        self.name = name
        self.age = age
leo = parrot("leo",5 ,"pink")
blu = parrot("blu",10,"blue")
woo = parrot("woo",15,"green")
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))
print("{} is {} years old {} color".format(blu.name,blu.age,blu.color))
print("{} is {} years old {} color".format(woo.name,woo.age,woo.color))
print("leo is a {}".format(leo.species))
print("{} is {} years old {} color".format(leo.name,leo.age,leo.color))