# Требуется вывести все целые степени двойки (т.е. числавида 2^k), не превосходящие числа N.
from os import system

system('cls')

number = int(input('Введите число: '))
k = 0
while 2 ** k < number:
    print(f"{2 ** k}", end='; ')
    k += 1
