my_list_1 = []
my_list = [57.8, 46.51, 97, 189.1, 37.48, 999.99, 5.3, 0.99, 5002.01, 36]
# A.
for numbers in my_list:
    if type(numbers) == float or int:
        my_list_1.append(f'{numbers // 1:.0f} руб {(numbers - numbers // 1)*100:02.0f} коп')
print(my_list_1)
# B.
before_sort = my_list[:]
my_list.sort()
print(my_list)
after_sort = my_list
print(before_sort.index(97))
print(after_sort.index(97))
print(id(before_sort[2]))
print(id(after_sort[6]))
# C.
sorted(my_list)
my_list2 = list(reversed(my_list))
print(my_list2)
# D.
print(my_list2[:5])


