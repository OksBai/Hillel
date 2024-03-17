class Calculator:
    def add(self, x, y):
        try:
            return x + y
        except Exception as e:
            return f"Помилка додавання: {e}"

    def subtract(self, x, y):
        try:
            return x - y
        except Exception as e:
            return f"Помилка вiднiмання: {e}"

    def multiply(self, x, y):
        try:
            return x * y
        except Exception as e:
            return f"Помилка множення: {e}"

    def divide(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Помилка! Ділення на нуль")
            return x / y
        except Exception as e:
            return f"Помилка ділення: {e}"

    def power(self, x, y):
        try:
            if y < 0:
                raise NegativePowerError("Помилка! Неможливо піднести число до від’ємного степеня")
            return x ** y
        except Exception as e:
            return f"Помилка піднесення до степеня: {e}"

    def square_root(self, x):
        try:
            if x < 0:
                raise ValueError("Помилка! Неможливо обчислити квадратний корінь із від’ємного числа")
            return x ** 0.5
        except Exception as e:
            return f"Помилка обчислення квадратного кореня: {e}"


class NegativePowerError(Exception):
    pass

calc = Calculator()
print("Addition:", calc.add(6, 8))
print("Subtraction:", calc.subtract(10, 4))
print("Multiplication:", calc.multiply(7, 2))
print("Division:", calc.divide(12, 4))
print("Exponentiation:", calc.power(2, 3))
print("Square root:", calc.square_root(16))
print("Division by zero:", calc.divide(5, 0))
print("Negative exponentiation:", calc.power(2, -3))
print("Square root of negative number:", calc.square_root(-9))
