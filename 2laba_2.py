my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
my_string=my_string.replace('_','')
my_string = my_string.split(';')
my_string.append("О студенте")
print(my_string)
print("%s%+9s%+9s%+21s" % (my_string[0],my_string[1],my_string[2],my_string[15]))
print("%-9s%-9s%-12s%-9s" % (my_string[5],my_string[6],my_string[7],my_string[8]+', '+my_string[9]))
print("%-9s%-9s%-12s%-9s" % (my_string[10],my_string[11],my_string[12],my_string[13]+', '+my_string[14]))
