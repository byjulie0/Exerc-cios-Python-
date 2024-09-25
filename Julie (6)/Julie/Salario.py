salario = float(input("Digite o seu salario"))
if salario < 500.00:
    a= salario +(salario*0.15)
    print(f'você recebe 15% de aumento seu novo salario será de R$:{a}')
elif salario <=1000:
    b= salario + (salario*0.10)
    print(f'você recebe 10% de aumento seu novo salario será de R$:{b}')
else:
    c= salario + (salario*0.5)
    print(f'você recebe 5% de aumento seu novo salario será de R$: {c}')