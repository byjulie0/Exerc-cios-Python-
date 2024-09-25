agenda = []
ordem_paciente = 0

while True:
    print("1-Usuário\n2-Médico")
    h = int(input("Selecione a opção desejada: "))

    if h == 1:
        op = print("1-Marcar uma Consulta\n2-Verificar historico de consultas\n3-Voltar")
        m = int(input("Selecione a opção desejada:  "))

        if m == 1:
            for i in range(1):
                d = {}
                d ["nome"] = input("informe seu nome: ")
                d ["cpf"] = int(input("Informe seu CPF: "))
                d ["idade"] = int(input("Informe sua idade: "))
                d ["horario"] = float(input("Informe o horário de sua consulta: "))
                d["senha"] = ordem_paciente
                agenda.append(d)
                ordem_paciente + 1
                print("Consulta Marcada com sucessso")
            
        elif m == 2:
            print(agenda)

        elif m == 3:
            break

            

    if h == 2:
            print("1-Ver lista de Pacientes\n2-Realizar Consulta\n3-Liberar Paciente\n4- Sair")
            m = int(input("Selecione a opção desejada:  "))

            if m == 1:
                print(agenda)
                        
            elif m == 2: 
                remover_paciente = int(input("Digite a senha do paciente:  "))
                agenda.pop(remover_paciente)
                print("Paciente atendido")
        
            elif m == 3:
                print("Paciente liberado")

            elif m == 4:
                break


            