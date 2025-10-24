"""student_data = {
    "id1":{"name":["sara"],
           "class":["v"],
           "subject_integration": ["english, math, science"]
           },
"id2":{"name":["david"],
           "class":["v"],
           "subject_integration": ["english, math, science"]
           },
"id3":{"name":["sara"],
           "class":["v"],
           "subject_integration": ["english, math, science"]
           },
"id4":{"name":["surya"],
           "class":["v"],
           "subject_integration": ["english, math, science"]
           },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)"""

test_dict = {"codingal" : 2, "is" : 2, "best" :2, "for": 2,"coding":1}
print("the organal dictionary")
k = 2
res=0
for key in test_dict:
    if test_dict[key] == k:
        res = res+1
print("frequency of k is :" + str(res))