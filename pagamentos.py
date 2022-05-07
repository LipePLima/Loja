#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:  – à vista dinheiro/cheque: 10% de desconto  – à vista no cartão: 5% de desconto  – em até 2x no cartão: preço formal   – 3x ou mais no cartão: 20% de juros

from time import sleep

print('{:=^60}'.format(' LOJAS LIMA '))
valor = float(input('\033[0;32mInforme o valor do produto:\033[m '))
print('-'*100)
sleep(1)
print('''As formas de pagamento são:
    [1] à vista em dinheiro/pix: 10% de desconto
    [2] à vista no cartão: 5% de desconto
    [3] Parcelando, terá 2 opções: ''')
print('-'*100)
pagamento = int(input('\033[0;32mEscolha a forma de pagamento:\033[m '))
if pagamento == 1:
    valor2 = valor - (valor*10)/100
    sleep(1)
    print('Ok! Calculando o novo valor')
    sleep(2)
    print()
    print(f'O valor descontado os 10% será R${valor2:.2f}.')
    sleep(1)
    print()
    print('Aguardando pagamento...')
    sleep(5)
    print()
    print('Obrigado por comprar na nossa loja. Volte sempre!')
elif pagamento == 2:
    valor3 = valor - (valor*5)/100
    sleep(1)
    print('Ok! Calculando o novo valor')
    sleep(2)
    print()
    print(f'O valor descontado os 5% será R${valor3:.2f}.')
    sleep(1)
    print()
    print('Aguardando pagamento...')
    sleep(5)
    print()
    print('Obrigado por comprar na nossa loja. Volte sempre!')
elif pagamento == 3:
    sleep(1)
    print('''   [1] em até 2x no cartão - preço formal
   [2] 3x ou mais no cartão - 20% de juros''')
    print('-'*100)
    escolha = int(input('\033[0;32mEscolha a forma de parcelamento:\033[m '))
    valor4 = valor + (valor*20)/100
    print('-'*100)
    if escolha == 1:
        print()
        sleep(2)
        print(f'Você pode parcelar em até 2x sem juros. O valor de cada parcela será de R${valor/2:.2f}.')
        sleep(1)
        print()
        print('Aguardando pagamento...')
        sleep(5)
        print()
        print('Obrigado por comprar na nossa loja. Volte sempre!')
    else:
        print()
        sleep(2)
        print(f'Você pode parcelar em 3x ou mais, mas com juros de 20% totalizando R${valor4:.2f}.')
        totparc = int(input('\033[0;32mEm quantas parcelas deseja pagar?:\033[m '))
        parc = valor4/totparc
        print()
        print(f'Sua compra será parcelada em {totparc}x, resultando num valor de R${parc:.2f} por mês!')
        sleep(1)
        print()
        print('Aguardando pagamento...')
        sleep(5)
        print()
        print('Pagamento aprovado.')
        print()
        sleep(1)
        print('Obrigado por comprar na nossa loja. Volte sempre!')
print('_'*100)
