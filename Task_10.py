# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
from random import randint
from os import system

system('cls')

quantity_coins = int(input('Введите колличество монет: '))
collection_coin = list(range(quantity_coins))

for i in range(quantity_coins):
    collection_coin[i] = randint(0, 1)

print(f"Монеты лежат на столе так: {collection_coin},где 1-орёл, 0-решка.")

if collection_coin.count(0) == quantity_coins or collection_coin.count(1) == quantity_coins:
    print(f"Все {quantity_coins} монет(ы) лежат вверх одной стороной.")
elif collection_coin.count(0) == collection_coin.count(1):
    print(f"Колличество монет одинаково и равно {collection_coin.count(0)}, неважно что переворачивать, монеты с решками или с орлами.")
elif collection_coin.count(0) < collection_coin.count(1):
    print(f"Необходимо перевернуть вверх {collection_coin.count(0)} монет(ы) с решкой (нулем)")
else:
    print(f"Необходимо перевернуть вверх {collection_coin.count(1)} монет(ы) с орлом (единицей)")