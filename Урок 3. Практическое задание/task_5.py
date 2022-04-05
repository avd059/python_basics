"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


# Функция определения является ли число числом, если нет то возвращаем 0
def is_integer(n):
    try:
        int(n)
    except ValueError:
        return 0
    else:
        return int(n)


my_last = ""
my_sum = 0
# Цикл пока не нажмем выход по заданному критерию
while my_last != "q":
    my_list = []
    my_list_temp = input("Введите числа через пробел, q выход , enter подитог: ").split()
    for i in my_list_temp:
        print(i)
        my_list.append(is_integer(i))
    print(f"Промежуточная сумма  {sum(my_list)}. ")
    for j in my_list_temp:
        if j == "q":
            my_last = "q"
    my_sum = my_sum + sum(my_list)
    # Условие чтобы при первом прогоне не печаталося итог
    if my_sum != sum(my_list):
        print(f"Сумма с нарастающим итогом {my_sum}")
