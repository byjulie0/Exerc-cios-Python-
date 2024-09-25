funcionarios = []
salario_maior = 0

for i in range(4):
    d = {}
    d ["nome"] = input("Digite seu nome: ")
    d ["funcao"] = input("Digite sua função: ")
    d ["salario"] = float(input("Digite seu salário: ")) 

    funcionarios.append(d)
    

    if d["salario"] > salario_maior:
        salario_maior = d["salario"]
       

for pessoa in funcionarios:
    if pessoa["salario"] == salario_maior:
      print(F"Funcionário com maior salário é {pessoa["nome"]}")
   