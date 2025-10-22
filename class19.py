"""empty_list = []
print()
numbers = [1,2,3,4,5]
print(numbers)
triples = [1,2,3]*3
print(triples)
aList = [100,200,300,400,500]
aList = aList[::-1]
print(aList,"n")"""

"""def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr+= 1
            lst.append(word)
    print("List of words with first and last character same\n",lst)
    return ctr
count = match_word(["abc","cfc","xyz","aba" "1221"])
print("number of words having first and last character :", count)"""

L = [4,5,1,2,9,7,10,8]
print("Origanal list:",L)
count = 0
for i in L:
    count+= i
avg = count/len(L)
print("sum =",count)
print("avarage=",avg)
L.sort()
print("smallest element is:",L[0])
print("largest element is:",L[-1])