import math
class RationalFractional:

    def __init__(self, num1 : int, num2 : int):
        self.numerator = num1 // math.gcd(num1, num2)
        if num2 != 0:
            self.denominator = num2 // math.gcd(num1, num2)
        else:
            raise ZeroDivisionError

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_sign(self):
        return (self.numerator / self.denominator) ** 0

    def __add__(self, other):
        if isinstance(other, int):
            if other >= 0:
                numerator = self.numerator + other * self.denominator
                denominator = self.denominator
                return RationalFractional(numerator, denominator)
            else:
                return self - other
        elif isinstance(other, RationalFractional):
            if other.get_sign():
                if self.denominator == other.denominator:
                    numerator = self.numerator + other.numerator
                    denominator = self.numerator
                    return RationalFractional(numerator, denominator)
                else:
                    numerator = self.numerator * other.denominator + other.numerator * self.denominator
                    denominator = self.denominator * other.denominator
                    return RationalFractional(numerator, denominator)
            else:
                return self - RationalFractional(abs(other.numerator), abs(other.denominator))
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, int):
            if other < 0:
                return self + abs(other)
            else:
                numerator = self.numerator - other * self.denominator
                denominator = self.denominator
                return RationalFractional(numerator, denominator)
        elif isinstance(other, RationalFractional):
            if other.get_sign():
                if self.denominator == other.denominator:
                    numerator = self.numerator - other.numerator
                    denominator = self.denominator
                    return RationalFractional(numerator, denominator)
                else:
                    numerator = self.numerator * other.denominator - other.numerator * self.denominator
                    denominator = self.denominator * other.denominator
                    return RationalFractional(numerator, denominator)
            else:
                return self + RationalFractional(abs(self.numerator), abs(self.denominator))
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return RationalFractional(self.numerator * other, self.denominator)
        elif isinstance(other, RationalFractional):
            return RationalFractional(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, int):
            return RationalFractional(self.numerator, self.denominator * other)
        elif isinstance(other, RationalFractional):
            return RationalFractional(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            raise TypeError

    def __pow__(self, power : int, modulo=None):
        return RationalFractional(self.numerator ** power, self.denominator ** power)


# Графическая обертка
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate():
  try:
    # Получение значений из полей ввода
    rf1 = RationalFractional(int(num1_entry.get()), int(den1_entry.get()))
    rf2 = RationalFractional(int(num2_entry.get()), int(den2_entry.get()))
    operation = operation_var.get()

    # Вычисление результата
    if operation == "+":
        result = rf1 + rf2
    elif operation == "-":
        result = rf1 - rf2
    elif operation == "*":
        result = rf1 * rf2
    elif operation == "/":
        result = rf1 / rf2

    result_label.config(text=str(result))  # Отобразить результат как строку

  except ValueError:
    result_label.config(text="Некорректные данные!")


# Создание главного окна
root = tk.Tk()
root.title("Калькулятор дробей")

# Первая дробь
num1_label = tk.Label(root, text="Числитель 1:")
num1_label.grid(row=0, column=0, padx=5, pady=5)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1, padx=5, pady=5)

den1_label = tk.Label(root, text="Знаменатель 1:")
den1_label.grid(row=1, column=0, padx=5, pady=5)
den1_entry = tk.Entry(root)
den1_entry.grid(row=1, column=1, padx=5, pady=5)

# Операция
operation_label = tk.Label(root, text="Операция:")
operation_label.grid(row=2, column=0, padx=5, pady=5)
operation_var = tk.StringVar(root)
operation_var.set("+")
operation_menu = ttk.Combobox(root, textvariable=operation_var, values=["+", "-", "*", "/"])
operation_menu.grid(row=2, column=1, padx=5, pady=5)

# Вторая дробь
num2_label = tk.Label(root, text="Числитель 2:")
num2_label.grid(row=3, column=0, padx=5, pady=5)
num2_entry = tk.Entry(root)
num2_entry.grid(row=3, column=1, padx=5, pady=5)

den2_label = tk.Label(root, text="Знаменатель 2:")
den2_label.grid(row=4, column=0, padx=5, pady=5)
den2_entry = tk.Entry(root)
den2_entry.grid(row=4, column=1, padx=5, pady=5)

# Кнопка "Посчитать"
calculate_button = tk.Button(root, text="Посчитать", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Вывод результата
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
