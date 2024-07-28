class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        try:
            amount = int(input('Введите сумму для внесения: '))
            self._balance += amount
            print(f'Новый баланс: {self._balance}')
        except ValueError:
            print('Пожалуйста, введите корректную сумму.')

    def _kill(self):
        self._balance = 0
        print('Баланс обнулен.')

    def __jackpot(self):
        self._balance *= 10
        print(f'Вы выиграли джекпот! Новый баланс: {self._balance}')

    def _merge_balance(self, other):
        if isinstance(other, Bank):
            self._balance += other._balance
            print(f'Баланс объединен. Новый баланс: {self._balance}')
        else:
            print('Ошибка: объект не является экземпляром класса Bank.')

class Calculator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value + other.value)
        return Calculator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value - other.value)
        return Calculator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.value * other.value)
        return Calculator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.value != 0:
                return Calculator(self.value / other.value)
            else:
                raise ValueError("Деление на ноль невозможно")
        if other != 0:
            return Calculator(self.value / other)
        else:
            raise ValueError("Деление на ноль невозможно")

    def __str__(self):
        return str(self.value)

bank1 = Bank('Макс', 100)
bank2 = Bank('Данчик', 200)

bank1.moneyX()
bank1._kill()
bank1._Bank__jackpot()
bank1._merge_balance(bank2)

calc1 = Calculator(10)
calc2 = Calculator(5)

print("Сложение:", calc1 + calc2)
print("Вычитание:", calc1 - calc2)
print("Умножение:", calc1 * calc2)
print("Деление:", calc1 / calc2)

print("Сложение с числом:", calc1 + 3)
print("Вычитание с числом:", calc1 - 3)
print("Умножение с числом:", calc1 * 3)
print("Деление с числом:", calc1 / 2)
