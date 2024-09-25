valor = int(input("Digite o valor da compra: "))
formadepagamento = int(input("Escolha sua forma de pagamento, 1- Á vista ou pix , 2- Á vista no cartão de crédito , 3- Em duas vezes , 4- Em três vezes: "))
if formadepagamento > 4 or formadepagamento < 1:
    print("Forma de pagamento não encontrada") 
if formadepagamento == 1:
    desconto = valor - (valor*0.10)
    print(f'Você recebeu 10% de desconto em sua compra, o valor total de sua compra é R${desconto}')
if formadepagamento == 2:
    desconto = valor - (valor*0.05)
    print(f'Você recebeu 5% de desconto em sua compra, o valor total de sua compra é R${desconto}')
if formadepagamento == 3:
    valorparcelado2 = valor/2
    print(f'Você pagará duas parcela de R${valorparcelado2}')
if formadepagamento == 4:
    valorparcelado3 = (valor/3 )+ valor*0.10
    print(f'Você pagará três parcelas de R${valorparcelado3} com 10% de juros')


    
