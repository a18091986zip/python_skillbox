# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
sum_ = 0
i = 0
while i < 10:
    if i == 0:
        pass
    else:
        expenses += expenses*0.03
    sum_ += expenses
    print(f'Расходы за {i+1} месяц: {expenses}')
    i += 1

print(f'Студенту надо попросить: {abs(educational_grant*10 - sum_)} рублей')