my_list_1 = []
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']
for value in my_list:
    my_list_1.append(value.split()[-1].capitalize())
for name in range(len(my_list_1)):
    out = f"'Привет,{my_list_1[name]}!'"
    print(out)

