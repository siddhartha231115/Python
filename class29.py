"""from abc import ABC,abstractmethod
class ABsclass(ABC):
    def print(self,x):
        print("Passed values:",x)
    @abstractmethod
    def task(self):
        print("we are ABsclass task")
class test_class(ABsclass):
    def task(self):
        print("we are inside test_class task")
test_obj = test_class()
test_obj.task()
test_obj.print(100)"""

"""from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
     def move(self):
         print("i can bark")
class lion(animal):
     def move(self):
         print("i can roar")
r = Human()
r.move()
k = snake()
k.move()
r = dog()
r.move()
k = lion()
k.move()"""

