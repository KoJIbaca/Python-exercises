def ai_calculate(term1, operation, term2):
    # Результат выполнения операции
    if operation == '+':
        print(term1 + term2)
    elif operation == '-':
        print(term1 - term2)
    elif operation == '*':
        print(term1 * term2)
    elif operation == '/':
        print(term1 / term2)
    elif operation == '//':
        print(term1 // term2)
    elif operation == '%':
        print(term1 % term2)
    else:
        print(pow(term1, term2))


def ask_key(key):
    while True:
        try:
            return float(input(f'Введите {key} число:\n'))
        except:
            print('Нельзя вводить выражения или буквы.')


def ask_op():
    # Ввод и проверка оператора
    print('''Выберите оператор:\n
            1. Для сложения введите - {}\n
            2. Для вычитания введите - {}\n
            3. Для умножения введите - {}\n
            4. Для деления введите - {}\n
            5. Для целочисленного деления введите - {}\n
            6. Для получения остатка от деления введите - {}\n
            7. Для возведения в степень введите - {}\n'''.format('+', '-', '*', '/', '//', '%', '^'))

    while True:
        ops_list = ['+', '-', '*', '/', '//', '%', '^']
        try:
            ops = input('Введите оператор:\n')
            if ops not in ops_list:
                print('Нельзя вводить выражения или числа!')
                continue
        except:
            pass
        else:
            break
    return ops


if __name__ == '__main__':
    stop_ops = ['/', '//', '%']

    a = ask_key('первое')
    ops = ask_op()

    correct = False
    while correct is False:
        b = ask_key('второе')
        if b == 0.0 and ops in stop_ops:
            print('На ноль делить нельзя!')
        else:
            correct = True


    ai_calculate(a, ops, b)