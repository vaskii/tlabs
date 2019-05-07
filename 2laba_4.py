print("")
print('Введите целочисленное кол-во элементов списка (не меньше 10)')

n = int(input("Кол-во элементов: "))
lst = []
i = 0
for i in range(1, n+1):
        lst.append(int(input("Введите " + str(i) + " число:")))
k=3
while k <= 7:
    lst.pop(k)
    k += 1
i=1
for i in range (1,3):
    lst.append(int(input("Введите дополнительное число: ")))
print(lst)