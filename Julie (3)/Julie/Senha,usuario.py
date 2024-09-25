usuarioUm = ["usuario_123", "usuario678","usuario_102"]
senhaUm = ["senha123", "usuario_678", "usuario_103"]

for i in usuarioUm:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite seu senha: ")
    
    if usuario in usuario:
        if senha != usuario:
            print("Usuário e senha válidos.")
            break
        else:
            print("Sua senha é igual ao seu usuário, Por Favor digite novamente") 
else:
     print("Usuário inválido, Por Favor tente novamente")