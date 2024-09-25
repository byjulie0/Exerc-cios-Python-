import random

class Bingo():
    def __init__(self):
        self.b = []
        self.i = []
        self.n = []
        self.g = []
        self.o = []

    def AdicionarNúmeros(self):
        self.b = random.sample(range(1, 16), 5)
        self.i = random.sample(range(16, 31), 5)
        self.n = random.sample(range(31, 46), 5)
        self.g = random.sample(range(46, 61), 5)
        self.o = random.sample(range(61, 76), 5)

    def NúmeroSorteado(self):
        self.numero = int(input("Digite o número sorteado: "))
        if self.numero in self.b:
            self.b[self.b.index(self.numero)] = "X"
        elif self.numero in self.i:
            self.i[self.i.index(self.numero)] = "X"
        elif self.numero in self.n:
            self.n[self.n.index(self.numero)] = "X"
        elif self.numero in self.g:
            self.g[self.g.index(self.numero)] = "X"
        elif self.numero in self.o:
            self.o[self.o.index(self.numero)] = "X"
        else:
            print("Número não encontrado na cartela.")

    def ValidarCartelaColuna(self):
        if all(num == "X" for num in self.b):
            print("Você fez Bingo na coluna B")
        if all(num == "X" for num in self.i):
            print("Você fez Bingo na coluna I")
        if all(num == "X" for num in self.n):
            print("Você fez Bingo na coluna N")
        if all(num == "X" for num in self.g):
            print("Você fez Bingo na coluna G")
        if all(num == "X" for num in self.o):
            print("Você fez Bingo na coluna O")

    def ValidarCartelaLinha(self):
        if all(num == "X" for num in self.b):
            print("Você fez Bingo na linha 1")
        if all(num == "X" for num in self.i):
            print("Você fez Bingo na linha 2")
        if all(num == "X" for num in self.n):
            print("Você fez Bingo na linha 3")
        if all(num == "X" for num in self.g):
            print("Você fez Bingo na linha 4")
        if all(num == "X" for num in self.o):
            print("Você fez Bingo na linha 5")

    def ValidarCartelaDiagonal(self):
        if self.b[0] == "X" and self.i[1] == "X" and self.n[2] == "X" and self.g[3] == "X" and self.o[4] == "X":
            print("Você fez Bingo na diagonal principal")

    def Cartela(self):
        print("-------Bem Vindo ao Bingo--------\nSua cartela é essa:")
        print(" B   I   N   G   O")
        for i in range(5):
            print(f"{self.b[i]:2} {self.i[i]:2} {self.n[i]:2} {self.g[i]:2} {self.o[i]:2}")

b = Bingo()
b.AdicionarNúmeros()
b.Cartela()

while True:
    b.NúmeroSorteado()
    b.Cartela()
