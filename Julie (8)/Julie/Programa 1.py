import random

class Sorteio:
    def __init__(self):
        self.numeros_sorteados = []

    def Sorteio(self):
        while True:
            self.numeros = random.randrange(1,75)
            if not self.numeros in self.numeros_sorteados:
                self.numeros_sorteados.append(self.numeros)
                return self.numeros
                # print(f"Seu número sorteado é {self.numeros}")

            if len(self.numeros_sorteados) >= 75:
                print("Todos os números já foram sorteados")
                break

    def FazerSorteio(self):
        while True:
            if len(self.numeros_sorteados) < 75:
                print("BEM -VINDO AO SOTEADOR DE BINGO!!!")
                print(" ")
                input("Aperte enter para iniciar: ")
                print(" ")
                self.Sorteio()
                self.Numero()
              
    def Numero(self):
        print(f"Números sorteados{self.numeros_sorteados}")
        print(f"{self.numeros}")

sorteio1 = Sorteio()
sorteio1.FazerSorteio()
sorteio1.Numero()
   


    