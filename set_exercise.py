
# Set is an unsorted unique list
a = set()
print(type(a)) # <class 'set'>
a = {}
print(type(a)) # <class 'dict'>
a = {5}
print(type(a)) # <class 'set'>
a = set()
a.add(1)
print(a) # {1}
a.add(1)
print(a) # {1} -- still the same because no duplciations in set
list1 = [1, 1 , 4 , 5 , 6 , 7, 1, 4, -3]
print(set(list1)) # {1, 4, 5, 6, 7, -3}

# create dictionary with duplicated values
# 1 : 'o' one
# 2 : 't' two
# 3 : 't'
# 4 : 'f'
# 5 : 'f'
# ... 10

# write a loop to display how many times
# each letter repeats itself

lettersDict = { 1: 'o', 2: 't', 3: 't', 4: 'f', 5: 'f', 6: 's', 7: 's', 8: 'e', 9: 'n', 10: 't'}

listOfvalues = list(lettersDict.values()) # ['o', 't', 't', 'f', 'f', 's', 's', 'e', 'n']
print(listOfvalues)
for value in sorted(set(listOfvalues)):
    print (f' \'{value}\' : { listOfvalues.count(value) } times')













