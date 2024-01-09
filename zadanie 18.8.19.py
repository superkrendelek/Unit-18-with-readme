    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        summa += 0
    elif 18 <= age < 25:
        summa += 990
    elif age >= 25:
        summa += 1390

print("Кол-во билетов: " + str(tickets) + "шт." )

if tickets > 3 :
    skidka = summa / 100 * 10
    itogo = summa - skidka
    print("Скидка составляет: " + str(skidka))
    print("Сумма к оплате: " + str(itogo))
if tickets < 4 :
    print("Сумма к оплате: " + str(summa))
