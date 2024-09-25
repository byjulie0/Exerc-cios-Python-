carrinho = []
compra_total = 0
listah = ["Higiene","Pasta de dente",3.50,"Sabonete",1.58,"Cotonete",4.00]
listap = ["Produtos para Casa","Rodo",23.71,"Vassoura",20.00,"Pá",17.30]
listaf = ["Alimento-Futa","Banana Nanica",5.99,"Maçã",14.99,"Kiwi",13.85]
listav = ["Alimento-Vegetais","Tomate",7.85,"Cebola",6.95,"Batata",10.50]
codigosp = ("Pasta de dente 10\nSabonete 20\nCotonete 30\nRodo 14\nVassoura 16\nPá 18\nBanana 1\nMaçã 3\nKiwi 6\nTomate 9\nCebola 12\nBatata 15\n")
estoque_pastadedente = 14
estoque_sabonete = 20
estoque_cotonete = 39
estoque_rodo = 4
estoque_vassoura = 10
estoque_pa_de_lixo = 8
estoque_banana = 17
estoque_maça = 25
estoque_kiwi = 6
estoque_tomate = 45
estoque_cebola = 60
estoque_batata = 50


while True:
    print(" ")
    print("Seja Bem-Vindo ao Super Mercado Vieira")
    print("1-Funcionario\n2-Cliente\n3-Sair")
     
    entrada = int(input())

    if entrada == 3:
        break
   
    elif entrada == 1:
        m = input("Digite sua matrícula: ")
        nf = input("Digite seu nome: ")
        cpff = input("Digite seu CPF: ")
        print(" ")
        print(f"Seja bem-vindo {nf}")
        print("1-Consultar estoque")
        print("2-Atualizar estoque")
        print("3-Adicionar novos produtos")
        print("4-Alterar Preço")
        print("5-Sair")
         
        opf = int(input("Selecione a ação a ser realizada: "))

        if opf == 1:
            print("Higiene ")
            print(" ")
            print(f'{estoque_pastadedente} pasta de dente disponíveis no estoque')
            print(f'{estoque_sabonete} sabonetes disponíveis no estoque')
            print(f'{estoque_cotonete} cotonetes disponíveis no estoque')
            print(" ")
               
            print("Produto para casa")
            print(" ")
            print(f'{estoque_rodo} rodos disponíveis no estoque')
            print(f'{estoque_vassoura} vassouras disponíveis no estoque')
            print(f'{estoque_pa_de_lixo} pás disponíveis noo estoque')
            print(" ")

            print("Alimento-Fruta")
            print(" ")
            print(f'{estoque_banana} bananas disponíveis no estoque')
            print(f'{estoque_maça} maçãs disponíveis no estoque')
            print(f'{estoque_kiwi} kiwis disponíveis no estoque')
            print(" ")

            print("Alimentos-Vegetais")
            print(" ")
            print(f'{estoque_tomate} tomates disponíveis no estoque')
            print(f'{estoque_cebola} cebola disponíveis no estoque')
            print(f'{estoque_batata} batatas disponíveis no estoque')


        elif opf == 2:
            itensc = int(input("Qual o código do produto que deseja adicionar: "))
            quantidade = int(input("Quantos produtos deseja adicionar: "))

            if itensc == 10:
                estoque_pastadedente += quantidade
            if itensc == 20:
                estoque_sabonete += quantidade
            if itensc == 30:
                estoque_cotonete += quantidade
            if itensc == 14:
                estoque_rodo += quantidade
            if itensc == 16:
                estoque_vassoura += quantidade
            if itensc == 18:
                estoque_pa_de_lixo += quantidade
            if itensc == 1:
                estoque_banana += quantidade
            if itensc == 3:
                estoque_maça += quantidade
            if itensc == 6:
                estoque_kiwi += quantidade
            if itensc == 9:
                estoque_tomate += quantidade
            if itensc == 12:
                estoque_cebola += quantidade
            if itensc == 15:
                estoque_batata += quantidade


        elif opf == 3:
            print("1-Higiene\n2-Produtos Para Casa\n3-Alimentos-Frutas\n4-Alimento-Vegetais")
            sessão = int(input("Digite o código da sessão do produto que deseja adicionar"))
               
            if sessão == 1:
                nome = input("Digite o nome do produto: ")
                quant =int(input("Digite a quantidade do produto que deseja adicionar:"))
                descricao = input("De uma breve descrição sobre o produto: ")
                preco = float(input("Digite o preço do produto: "))
                codigopn =int(input("Digite o código do produto: "))
                listah.append(nome)
                listap.append(preco)
                codigosp = codigopn
                             
            elif sessão == 2:
                nome = input("Digite o nome do produto: ")
                quant =int(input("Digite a quantidade do produto que deseja adicionar:"))
                descricao = input("De uma breve descrição sobre o produto: ")
                preco = float(input("Digite o preço do produto: "))
                codigopn =int(input("Digite o código do produto: "))
                listap.append(nome)
                listap.append(preco)
                codigosp = codigopn

            elif sessão == 3:
                nome = input("Digite o nome do produto: ")
                quant =int(input("Digite a quantidade do produto que deseja adicionar:"))
                descricao = input("De uma breve descrição sobre o produto: ")
                preco = float(input("Digite o preço do produto: "))
                codigopn =int(input("Digite o código do produto: "))
                listaf.append(nome)
                listap.append(preco)
                codigosp = codigopn

            elif sessão == 4:
                nome = input("Digite o nome do produto: ")
                quant =int(input("Digite a quantidade do produto que deseja adicionar:"))
                descricao = input("De uma breve descrição sobre o produto: ")
                preco = float(input("Digite o preço do produto: "))
                codigopn =int(input("Digite o código do produto: "))
                listav.append(nome)
                listap.append(preco)
                codigosp = codigopn

            elif opf == 4:
                print(codigosp)
                alterar_preco = int(input("Digite o código do produto que deseja alterar o preço: "))

                if alterar_preco == 10:
                    pasta_de_dente = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 20:
                    sabonete = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 30:
                    cotonete = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 14:    
                    rodo = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 16:
                    vassoura = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 18:
                    pa = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 1:  
                    banana = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 3:
                    maça = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 6:
                    kiwi = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 9:
                    tomate = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 12:
                    cebola = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

                if alterar_preco == 15:
                    batata = float(input("Digite o novo preço do produto: "))
                    print("O preço do produto foi alterado com sucesso")

            elif opf == 5:
                print("Você está voltando a página inícial")
                break

    elif entrada == 2:
        nc = input("Digite seu nome: ")
        cpfc = input("Digite seu CPF: ")
        print(f"Seja bem-vindo {nc}")
        print(" ")
        print("1-Visualizar Sessões")
        print("2-Visualizar Carrinho ")
        print("3-Adicionar ao Carrinho")
        print("4-Remover do carrinho")
        print("5-Finalizar compra")
        print("6-Sair")
               
        op = int(input("Selecione a ação a ser realizada: "))

        if op == 6:
            print("Você está voltando a página inícial")
            break
           

        elif op == 1:
            print(listah)
            print(listap)
            print(listaf)
            print(listav)
            print(codigosp)
               
        elif op == 2:
            if carrinho:
                for i in carrinho:
                    print(f'{i[0]} : R$ {i[1]}')
                    print(f'O valor da sua compra é R$:{compra_total}')
            else:
                print("Seu carrinho está vazio")
       
        elif op == 3:
            adicionar = int(input("Digite o código do produto que deseja adicionar ao carrinho: "))
               
            if adicionar == 10:
                carrinho.append("Pasta de dente")
                compra_total += 3.50

            elif adicionar == 20:
                carrinho.append("Sabonte")
                compra_total += 1.58

            elif adicionar == 30:
                carrinho.append("Cotonete")
                compra_total += 4.00
                         
            elif adicionar == 14:
                carrinho.append("Rodo")
                compra_total += 23.71

            elif adicionar == 16:
                carrinho.append("Vassoura")
                compra_total += 20.00

            elif adicionar == 18:
                carrinho.append("Pá de Lixo")
                compra_total += 17.30

            elif adicionar == 1:
                carrinho.append("Banana Nanica")
                compra_total += 5.99

            elif adicionar == 3:
                carrinho.append("Maçã")
                compra_total += 14.99

            elif adicionar == 9:
                carrinho.append("Kiwi")
                compra_total += 13.85
                         
            elif adicionar == 9:
                carrinho.append("Tomate")
                compra_total += 7.85

            elif adicionar == 12:
                carrinho.append("Cebola")
                compra_total += 6.95

            elif adicionar == 15:
                carrinho.append("Batata")
                compra_total += 10.50

        elif op == 4:
            if carrinho:
                print("Seu carrinho está vazio ")

            else:
                print(carrinho)
           
            remover_produto = int(input("Digite o código do produto que deseja remover"))
           
            if remover_produto in carrinho:
                carrinho.remove(remover_produto)
                print("Produto removido do carrinho")
            else:
                print("Produto não encontrado")
        elif op == 5:
            while True:
                print("1-Cartão de Crédito")
                print("2-Cartão de Débito")
                print("3-Voucher")
                print("4-Dinheiro")
                print("5-Pix")
                forma_de_pagamento = int(input("Qual a sua forma de pagamento"))

                # cartão de crédito
                if forma_de_pagamento == 1:
                    imposto_nacional = compra_total * 0.05
                    imposto_estadual = compra_total * 0.08
                    imposto_municipal = compra_total * 0.12
                    imposto_total = imposto_nacional + imposto_estadual + imposto_municipal
                    compra_com_impostos = compra_total + imposto_total
                    print(f"Sua compra total de R${compra_total}")
                    print(f'Volor da compra com o imposto nacional é {imposto_nacional}')
                    print(f'Volor da compra com o imposto estadual é {imposto_estadual}')
                    print(f'Volor da compra com o imposto municipal é {imposto_municipal}')
                    print(f'Sua compra total com os impostos é de R${compra_com_impostos}')
                   
                    quantcc = float(input("Informe o seu saldo: "))
                    senhacc  = int(input("Digite sua senha: "))

                    if quantcc >= compra_com_impostos:
                        print("Seu pagamento foi realizado com sucesso")
                         
                    else:
                        print("Seu saldo é insuficiente,escolha outra opção de pagamento")

                #    cartão de débito  
                elif forma_de_pagamento == 2:
                    imposto_nacional = compra_total * 0.05
                    imposto_estadual = compra_total * 0.08
                    imposto_municipal = compra_total * 0.12
                    imposto_total = imposto_nacional + imposto_estadual + imposto_municipal
                    compra_com_impostos = compra_total + imposto_total
                    print(f"Sua compra total de R${compra_total}")
                    print(f'Volor da compra com o imposto nacional é {imposto_nacional}')
                    print(f'Volor da compra com o imposto estadual é {imposto_estadual}')
                    print(f'Volor da compra com o imposto municipal é {imposto_municipal}')
                    print(f'Sua compra total com os impostos é de R${compra_com_impostos}')
                   
                    quantcd = float(input("Informe o seu saldo: "))
                   
                    if quantcd <= compra_com_impostos or quantcd == compra_com_impostos:
                        senhacd  = int(input("Digite sua senha: "))
                        print("Seu pagamento foi realizado com sucesso")
                               
                    else:  
                        print("Seu saldo é insuficiente,escolha outra opção de pagamento")

                # voucher  
                elif forma_de_pagamento == 3:
                    imposto_nacional = compra_total * 0.05
                    imposto_estadual = compra_total * 0.08
                    imposto_municipal = compra_total * 0.12
                    imposto_total = imposto_nacional + imposto_estadual + imposto_municipal
                    compra_com_impostos = compra_total + imposto_total
                    print(f"Sua compra total de R${compra_total}")
                    print(f'Volor da compra com o imposto nacional é {imposto_nacional}')
                    print(f'Volor da compra com o imposto estadual é {imposto_estadual}')
                    print(f'Volor da compra com o imposto municipal é {imposto_municipal}')
                    print(f'Sua compra total com os impostos é de R${compra_com_impostos}')
               
                    quantv = float(input("Digite o saldo da sua conta:"))
                    senhav  = int(input("Digite sua senha: "))
                
                    if quantv >= compra_com_impostos:
                        print(" ")
                        print(f'Seu troco é R${troco}')
                        print("Seu pagamento foi realizado com sucesso")
                        
                                   
                    else:
                        print("Seu saldo é insuficiente,escolha outra opção de pagamento")

                #    dinheiro  
                elif forma_de_pagamento == 4:
                    imposto_nacional = compra_total * 0.05
                    imposto_estadual = compra_total * 0.08
                    imposto_municipal = compra_total * 0.12
                    imposto_total = imposto_nacional + imposto_estadual + imposto_municipal
                    compra_com_impostos = compra_total + imposto_total
                    print(f"Sua compra total de R${compra_total}")
                    print(f'Volor da compra com o imposto nacional é {imposto_nacional}')
                    print(f'Volor da compra com o imposto estadual é {imposto_estadual}')
                    print(f'Volor da compra com o imposto municipal é {imposto_municipal}')
                    print(f'Sua compra total com os impostos é de R${compra_com_impostos}')
               
                    quantd = float(input("Digite a quantia de dinheiro :"))
                    troco = quantd - compra_com_impostos
                   
                    if quantd >= compra_com_impostos:
                        print(" ")
                        print(f'Seu troco é R${troco}')
                        print("Seu pagamento foi realizado com sucesso")
                    else:
                        print("Seu saldo é insuficiente,escolha outra opção de pagamento")
                       
                # pix
                elif forma_de_pagamento == 5:
                    imposto_nacional = compra_total * 0.05
                    imposto_estadual = compra_total * 0.08
                    imposto_municipal = compra_total * 0.12
                    imposto_total = imposto_nacional + imposto_estadual + imposto_municipal
                    compra_com_impostos = compra_total + imposto_total
                    print(f"Sua compra total de R${compra_total}")
                    print(f'Volor da compra com o imposto nacional é {imposto_nacional}')
                    print(f'Volor da compra com o imposto estadual é {imposto_estadual}')
                    print(f'Volor da compra com o imposto municipal é {imposto_municipal}')
                    print(f'Sua compra total com os impostos é de R${compra_com_impostos}')
                   
                    quantpix = float(input("Digite o saldo da sua conta:"))
                    senhapix  = int(input("Digite sua senha: "))
                    troco = quantpix - compra_com_impostos
                   
                    if quantpix <= compra_com_impostos:
                        quantpix = float(input("Digite o saldo da sua conta:"))
                    
                        print(" ")
                        print("Seu pagamento foi realizado com sucesso")
                    else:
                        print("Seu saldo é insuficiente,escolha outra opção de pagamento")