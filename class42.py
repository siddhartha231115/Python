import numpy as np
data_type = [("name","S15"),("class",int),("height",float)]
students_details = [("thejas",4,141),("anav",4,132),("praneel",4,139),("siddhartha",4,138)]
students = np.array(students_details,dtype=data_type)
print("origanal array:")
print(students)
print("sort by height")
print(np.sort(students,order="height"))