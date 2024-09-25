tarefa = []
codigo_tarefa = 1

while True:
    print(" ")
    print("1-Adicionar Tarefa")
    print("2-Listar Tarefa")
    print("3-Marcar Tarefa Como Concluída ")
    print("4-Remover Tarefa ")
    print("5-Sair ")
    print(" ")
    op = int(input("Selecione a opção desejada: "))

    if op == 1:
                d = {}
                d ["Descricao"] = input("Digite a descrição da tarefa: ")
                d ["status"] = input("Digite o status da tarefa: ")
                d ["Ordem"] = codigo_tarefa               
                codigo_tarefa += 1
                tarefa.append(d)
                print(tarefa)
             

    if op == 2:
            print(tarefa)
    else:
            print("Sua lista está vazia")

    if op == 3:
             for i in range(len(tarefa)):
              ordem_satus = int(input("Digite a ordem da tarefa: "))
              d ["status"] = input("Digite o status da tarefa: ")
              print(tarefa)              

    if op == 4:
            for i in range(len(tarefa)):
                remover = int(input("Digite a ordem da tarefa que deseja remover: "))
                tarefa.pop(remover)
                codigo_tarefa -= 1
                print("Sua tarefa foi removida com sucesso")
                break

            for i in range(len(tarefa)):
                if tarefa[i]["Ordem"] > remover:
                    tarefa[i]["Ordem"] -= 1


    if op == 5:
            print("Encerrando Sistema")
            break





            
        
