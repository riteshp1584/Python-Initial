
'''

list_1 = [i for i in range(1, 11)]

list_1.append(20)

print(list_1)

'''

'''

this_list = ["apple", "banana", "cherry", "orange", "strawberry", "pear"]

print(this_list[4])

print(this_list[-3])

this_list.pop(1)

print(this_list)

'''

'''
this_list_2 = ["apple", "banana", "cherry", "orange", "strawberry", "pear", "blueberry", "mango"]

print(sorted(this_list_2))

'''

list_2 = [i for i in range(1, 11)]

list_2.remove(5)

print(list_2)

print(list_2.index(6))

list_3 = [i for i in range(30, 35)]

list_2.append(list_3)

print(list_2)

list_4 = [i for i in range(50, 55)]

list_2.extend(list_4)

print(list_2)

if 30 in list_3:
    print("Yes")
else:
    print("No")
