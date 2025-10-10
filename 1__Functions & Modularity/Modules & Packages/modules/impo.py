import cryptography
print(cryptography.__version__) 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import random
from random import randint
from random import choice
randint(1,6)

def crypto_password():
    random_bytes = os.urandom(32)
    # Дополнительная обработка через хеш-функцию
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(random_bytes)
    return digest.finalize().hex()[:20]
players=['charles', 'martina', 'michael', 'florence', 'eli']
first_up=choice(players)
print(first_up)

""" создайте класс Die с одним атрибутом sides, который имеет значение по 
умолчанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до количества 
граней на кубике. Создайте экземпляр, представляющий 6-гранный кубик, и смоделируйте 
10 бросков.
Создайте экземпляры, представляющие 10- и 20-гранный кубик. Смоделируйте 10 бросков 
каждого кубика."""
class Die():
    def __init__(self,nums=6):
        self.nums=nums 
    def roll_die(self):
        run=randint(1,6)
        print(run)
de=Die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()
de.roll_die()


"""создайте список или кортеж, содержащий серию из 10 чисел и 5 букв. Случайным образом выберите 
4 числа или буквы из списка.
 Выведите сообщение о том, что 
билет, содержащий эту комбинацию из четырех цифр или букв, является выигрышным."""
class Lottery():
    def __init__(self,):
        self.pool=['a','f','n','u','d','b','m','k',1,5,3,4,9,0,6]
   
    def simulate_until_win(self, target_ticket):
        attempts = 0
        while True:
            attempts += 1
            drawn_ticket = random.sample(self.pool, 4)
            print(f"Выигрышная комбинация: {drawn_ticket}")
            # Сравниваем ПОСЛЕДОВАТЕЛЬНОСТИ - порядок важен
            if drawn_ticket == target_ticket:
                print("Это точное совпадение последовательности!")
                return attempts, drawn_ticket
            

# Использование
lottery = Lottery()
my_ticket = ['k', 'b', 1, 4]
attempts, winning_combo = lottery.simulate_until_win(my_ticket)
print(f"Ваш билет: {winning_combo}")
print(f'Потребовалось {attempts} попыток')
