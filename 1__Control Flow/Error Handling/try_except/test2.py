from datetime import datetime
class HungryCatError(Exception):
    def __init__(self, food, attempts=0):
        self.food = food
        self.attempts = attempts
        super().__init__(f"Кот отказался есть {food} {attempts} раз!")
    
    def try_again(self):
        self.attempts += 1
        return self.attempts < 3  #3 попытки

cat_food = "овощи"
error = HungryCatError(cat_food)

while error.try_again():
    print(f"накормить кота {cat_food}...")
    # raise error  
print("Кот голодный, нужна рыба!")

class CryptoWalletError(Exception):
    pass

class NotEnoughCryptoError(CryptoWalletError):
    def __init__(self, currency, balance):
        self.currency = currency
        self.balance = balance
        super().__init__(f"Не хватает {currency}. Баланс: {balance}")

def make_transaction():
    try:
        #симуляцмя ошибки
        raise ValueError("Неверный формат транзакции")
    except ValueError as e:
        raise NotEnoughCryptoError("BTC", 0.5) from e

try:
    make_transaction()
except CryptoWalletError as e:
    print(f"Ошибка кошелька: {e}")
    print(f"Причина: {e.__cause__}")  #оригинальная ошибка


class SelfHealingError(Exception):
    def __init__(self, problem):
        self.problem = problem
        self.solution = None
        super().__init__(problem)
    
    def fix(self):
        if "база данных" in self.problem:
            self.solution = "Перезагрузи PostgreS"
            return True
        return False

error = SelfHealingError("Не могу подключиться к базе данных")
if error.fix():
    print(f"автофикс: {error.solution}")
else:
    print("не могу починить")


class ZombieError(Exception):#жизни
    def __init__(self):
        self.lives = 3
        super().__init__("Zombie апокалипсис!")
    
    def __str__(self):
        self.lives -= 1
        return f"{super().__str__()} осталось жизней: {self.lives}"

try:
    raise ZombieError()
except ZombieError as e:
    print(e)  #осталось жизней 2
    print(e)  #осталось жизней 1
    print(e)  #осталось жизней 0


class PuzzleError(Exception):#ошибка-пазл
    pieces = []
    
    def __init__(self, piece):
        self.pieces.append(piece)
        if len(self.pieces) == 3:
            super().__init__("пазл собран: " + "".join(self.pieces))
        else:
            super().__init__(f"Добавлена часть: {piece}")

try:
    raise PuzzleError("Ош")
except PuzzleError as e:
    print(e)  

try:
    raise PuzzleError("иб")
except PuzzleError as e:
    print(e) 

try:
    raise PuzzleError("ка")
except PuzzleError as e:
    print(e)  