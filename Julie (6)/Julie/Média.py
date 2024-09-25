nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
média = (nota1+ nota2 + nota3/3)
if média>= 7:
    print("Aprovado")
if média < 7:
    print("Reprovado")
if média == 10:
    print("Aprovado")