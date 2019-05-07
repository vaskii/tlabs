import os,sys
def sure():
    v=input("Вы хотите продолжить?\ny-да,n-нет\n>> ")
    if v == "y":
        menu()
    elif v == "n":
        print("Завершение работы.")
        quit()
    else:
        print("Ответ не распознан.")
        print("=================")
        sure()
def count ():
    print("Файлов в папке: " + str(len([name for name in os.listdir('.') if os.path.isfile(name)])))
    print("=================")
    sure()
def file():
    print("Открываем файл")
    print()
    f = open("products.txt", "r")
    i=0
    n_l = f.read().splitlines()
    for check in n_l:
        n_l[i] = check.split(';')
        i += 1
    print("Строка: " + str(n_l) + "\n")
    print("Таблица:" + "\n")
    header = n_l.pop(0)
    print("%-3s%-25s%-8s%-10s" % (header[0], header[1], header[2], header[3]))
    price=[]
    print()
    i=0
    while i<3:
        price.append(n_l[i])
        i+=1
    n_l.sort(key=lambda x: x[2])
    for elem in n_l:
        print("%-3s%-25s%-8s%-10s" % (elem[0], elem[1], elem[2], elem[3]))
    print("=================")
    sure()
def price():
    k = 0
    f = open("products.txt")
    n_l = f.read().splitlines()
    for elem in n_l:
        n_l[k] = elem.split(';')
        k += 1
    header = n_l.pop(0);
    print("%-3s%-25s%-8s%-10s" % (header[0], header[1], header[2], header[3]))
    n_l.sort(key=lambda x: x[0])
    for elem in n_l:
        print("%-3s%-25s%-8s%-10s" % (elem[0], elem[1], elem[2], elem[3]))
    print("=================")
    print("Введите номер товара, цену которого хотите изменить:")
    num = input('>> ')
    print("Введите изменение цены: ")
    quantity = input(">> ")
    for elem in n_l:
        if elem[0] == num:
            print("Товар: {}".format(elem))
            elem[2] = int(elem[2]) + int(quantity)
            print("Измененный товар: {}".format(elem))
    v = input("Сохранить измененный список товаров в файл? (y/n)" + "\n>> ")
    if v == "y":
        f = open("products_upd.txt", "w")
        f.write(str(header) + '\n')
        for elem in n_l:
            f.write(str(elem) + '\n')
        print('Файл записан!')
        sure()
    else:
        print("Завершение работы.")
        quit()
def menu():
    print("Меню:\n0 - Выход\n1 - Посчитать файлы в директории\n"
          "2 - Вывод информации о товарах, сортированных по значению"
          "\n3 - Изменение количества товаров указанных номеров")
    m = input(">> ")
    if m == "0":
        sys.exit()
    if m == "1":
        count()
    if m == "2":
        file()
    if m == "3":
        price()
    else:
        print("Ответ не распознан.")
        print("=================")
        menu()
menu()