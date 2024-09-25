numero = int(input("Digite um numero: "))
if numero < 1000:
    print("numero inválido.Digite um numero menor que 1000.")
centena = numero // 100 
dezena = (numero - centena *100) // 10
unidade = numero - centena *100 - dezena *10
if centena > 0:
    print(f"{centena},centena(s),{dezena},dezena(s) e {unidade} unidade(s)")
elif dezena > 0:
    print(F"{dezena} dezena(s) e {unidade} unidade(s)")
else:
    print(f"{unidade} unidade(s)")


