# функція calc,прицмає два цілих числа та один знак арифметичної операції (+ - / *) та повертає результат
# виконання цієї операції.
# Повертати виключення ValueError, якщо числа не цілі, або нема знаку арифметичної операції.

def calc(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):  # перевірка на наявність знаків '+-/*'
        raise ValueError(f'Вираз повинен містити хоча б один знак ({allowed})')
    for sign in allowed:  # для кожного знаку в '+-/*'
        if sign in expression:  # якщо він є у виразі, спробувати провести обчислення
            try:
                left, right = expression.split(sign)  # ділимо вираз по знаку на left і right
                left, right = int(left), int(right)  # переводимо дві частини виразу в цілі числа
                # if sign == '+':  # основні операції:
                #     return left + right
                # elif sign == '-':
                #     return left - right
                # elif sign == '/':
                #     return left / right
                # elif sign == '*':
                #     return left * right
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Вираз повинен містити два цілих числа і тільки один знак')


if __name__ == '__main__':
    print(calc('2/8'))
