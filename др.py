num_1 = input('Введите ваш день рождения в формате 01 01 2000:')
num_2 = input('Введите сегодняшнее число в формате 01 01 2000:')
th = ['01','03','05','07','08','10','12']
sum=0
for i in range(1,int(num_1[3:5])):
    for j in th:
        if i == int(j):
            sum+=31
        elif i == 2:
            sum+=28
        else:
            sum+=30
sum += int(num_1[:2])
sum_1 = 0
for i in range(1,int(num_2[3:5])):
    for j in th:
        if i == int(j):
            sum_1+=31
        elif i == 2:
            sum_1+=28
        else:
            sum_1+=30
sum_1 += int(num_2[:2])
print(sum)
print(sum_1)
print(f'До вашего дня рождения осталось:{sum-sum_1}')