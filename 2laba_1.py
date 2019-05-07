my_string = "Heard you say you wanna die, so do I " \
"Just do it like Nike, eat the night " \
"Heard you said you wanna play, then it's Fisher Price " \
"Your shoes faker than my smile, not surprised"
my_string=my_string.replace(',','')
my_string = my_string.split(' ')
my_list=[]
k = 0
while k < len(my_string):
    j = len(my_string[k])
    if j in range (5,10):
        my_list.append(my_string[k])
    k += 1
print('Строка: ', my_list)
