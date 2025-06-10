
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