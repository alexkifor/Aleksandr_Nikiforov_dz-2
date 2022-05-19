my_list_1 = []
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for element in my_list:
    if element.isdigit():
        my_list_1.append(f'"{int(element):02d}"')
    elif element is str('+5'):
        pass
    else:
        my_list_1.append(element)
for i in my_list[8]:
    if i.isdigit():
        my_list_1.insert(8, f'"+{int(i):02d}"')
print(' '.join(my_list_1))
