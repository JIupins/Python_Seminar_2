# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Квадратное уравнение: ax^2 + bx + c =0.
# Дискриминант уравнения: D = b^2 − 4ac, если D < 0 то корней нет, D = 0 есть x1, D > 0 есть x1 и x2.
# Корни уравнения: x1=(-b+sqrt(D))/2a и x2=(-b-sqrt(D))/2a.
from os import system
import math

system('cls')

def Create_number(phrase):
    number = int(input(f"{phrase}: "))
    return number

def Find_numbers(one, two):
    D = one ** 2 - 4 * 1 * two
    if D < 0:
        print(f"Таких чисел не существует!")
    else:
        y1 = (-one + math.sqrt(D)) / 2 * (-1)
        x1 = one - y1
        print(f"Петя загадал два числа {y1} и {x1}")

num_one = Create_number("Введите сумму натуральных чисел")
num_two = Create_number("Введите произведение натуральных чисел")

Find_numbers(num_one, num_two)
