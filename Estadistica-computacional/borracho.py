import random
import os
os.system("cls")

class Borracho:
    def __init__(self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina():
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])