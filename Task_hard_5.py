# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.
from os import system
import math

system('cls')

def Create_number(phrase):
    number = int(input(f"{phrase}: "))
    return number

def Create_coordinates(num):
    collect_directs = [None] * num
    count1 = 0
    while count1 < len(collect_directs):
        collect_directs[count1] = [None] * 2
        count2 = 0
        while count2 < len(collect_directs[count1]):
            collect_directs[count1][count2] = int(input(f"Введите координаты точки {count1}.{count2}: "))
            count2 += 1
        count1 += 1
    return collect_directs

def Calculate_distance(coll):
    sum = 0
    count = 0
    while count < len(coll):
        sum += (coll[count][1] - coll[count][0])**2
        count += 1
    total = math.sqrt(sum)
    print(f"Расстояние между точками в {len(coll)}-мерном пространстве равно: {round(total,2)}")

quant_spaсes = Create_number("Введите колличество рассматриваемых пространств")
collection_directs = Create_coordinates(quant_spaсes)
Calculate_distance(collection_directs)
