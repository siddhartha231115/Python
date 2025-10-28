"""my_set = {1,2,3}
print(my_set)
my_set = {1.0 ,"hello",(1,2,3)}
print(my_set)
my_set = {1,2,3,4,3,2}
print(my_set)
my_set = set([1,2,3,2,])
print(my_set,"\n")
num_set = set([0,1,2,3,4,5])
print("oraginal ser:")
print(num_set)
print( "AFter inexing:")
print(num_set)"""

"""setx = {"green","blue"}
sety = {"blue", "yellow"}
print(setx)
print(sety)
print("\nintersection of two said sets:")
setz =setx.intersection(sety)
print(setz)"""
import array as arr
array_num = arr.array("i",[1,3,5,3,7, 9,3])
print("origanal array:"+str(array_num))
print("number of occurrences of the number 3 in te array:"+str(array_num.count(3)))
array_num.reverse()
print("revers the order of the items:")
print(str(array_num))