# Sistema de cadastro de usuários

usuarioUm_nome = "alice"
usuarioUm_senha = "1234"

usuarioDois_nome = "bob"
usuarioDois_senha = "abcd"

usuarioTres_nome = "carol"
usuarioTres_senha = "9876"

print("Bem-vindo ao sistema de cadastro de usuários!")

opcao = int(input("Escolha uma opção - 1: Login, 2: Cadastro:, 3: Calcular Consumo de Água "))

if opcao == 1: 
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if (usuario == usuarioUm_nome and senha == usuarioUm_senha) or (usuario == usuarioDois_nome and senha == usuarioDois_senha) or (usuario == usuarioTres_nome and senha == usuarioTres_senha):
        print("Login bem-sucedido!") 
else:
     print("Nome de usuário ou senha incorretos!")
if opcao == 2:
    print("Cadastre-se") 

    novo_usuario_nome = input("Digite seu novo nome de usuário: ")
    novo_usuario_senha = input("Digite sua nova senha: ")
    print("Cadastro realizado com sucesso!")

    print("Obrigado por utilizar nosso sistema!")

if opcao == 3:
    consumo_total = int(input("Digite o consumo total de água (em metros cúbicos): "))
    numero_pessoas = int(input("Digite o número de pessoas na residência: "))
    dias = (input("Digite o número de dias do período de consumo: "))
    consumo_por_pessoa_por_dia = consumo_total / (numero_pessoas * dias) 

    if consumo_por_pessoa_por_dia > 200:
        print("O consumo de água da residência está elevado.")

    elif consumo_por_pessoa_por_dia >= 100:
        print("O consumo de água da residência está moderado.")
    else:
        print("O consumo de água da residência está abaixo da média.")
