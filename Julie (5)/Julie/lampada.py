lampada = False

def ligarLampada():
    return True

def desligarLampada():
    return False

def consultarLampada():
    if lampada:
        print("Acesa")
    else:
        print("Desligada")
      
while True:
    print("1-Ligar Lampada")
    print("2-Desligar Lampada")
    print("3-Consultar Lampada")
    op = int(input("Digite a opção: "))

    if op == 1:
        lampada = ligarLampada()
    elif op == 2:
        lampada = desligarLampada()
    elif op == 3:
        consultarLampada()
