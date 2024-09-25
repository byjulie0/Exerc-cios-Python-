def exibeMenu ():
    print("")
    print("---Menu---\n")
    print("0-Sair")
    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplica")
    print("4-Dividir\n")
    
    opcao = int(input("escolha a opção desejada: "))
    print("")
    return opcao

def somar (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtrair (numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicar (numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def dividir (numero1, numero2):
    resultado = numero1 / numero2
    return resultado

i = 0
opcao = 0
num1 = 0
num2 = 0
resultado = 0

while opcao == 0:
    opcao = exibeMenu ()
    
    if opcao <= 0:
        break

    num1 = float(input("Informe o primeiro número para a operação: "))
    mum2 = float(input("Informe o segundo número para a operação: "))
    

if opcao == 1:
    resultado = somar (num1,num2)
    print(f"Resultado: {resultado}" )

elif opcao == 2:
    resultado = subtrair (num1,num2)
    print(f"Resultado: {resultado}")

elif opcao == 3:
    resultado = multiplicar (num1,num2)
    print(f"Resultado: {resultado}")

elif opcao == 4:
    resultado = dividir (num1,num2)
    print(f"Resultado: {resultado}")


    