my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my_string=my_string.replace('_','')
my_string = my_string.split(';')
my_list=[]
k = 0
while k < len(my_string):
    j = len(my_string[k])
    if j in range (5,10):
        my_list.append(my_string[k])
    k += 1
print('Строка: ', my_list)
