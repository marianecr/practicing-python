"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal 
- 3x ou mais no cartão: 20% de juros"""

preco = float(input('Insira o preço do produto: R$'))
opcao_pagamento = int(input('''Qual a forma de pagamento você deseja: 
                            1 - À VISTA COM DINHEIRO / CHEQUE (10% DE DESCONTO)
                            2 - À VISTA NO CARTÃO (5% DE DESCONTO)
                            3 - ATÉ 2X NO CARTÃO (SEM DESCONTO)
                            4 - 3X OU MAIS VEZES NO CARTÃO (20% DE JUROS)
                            >>> '''))

if opcao_pagamento == 1:
    valor_a_pagar = preco - (preco * 0.1)
    print(f'À vista com dinheiro / cheque - Preço final: R${valor_a_pagar:.2f}')

elif opcao_pagamento == 2:
    valor_a_pagar = preco - (preco * 0.05)
    print(f'À vista no cartão - Preço final: R${valor_a_pagar:.2f}')

elif opcao_pagamento == 3:
    print(f'Até 2x no cartão - Preço final: R${preco:.2f}')

elif opcao_pagamento == 4:
    valor_a_pagar = preco + (preco * 0.2)
    qtde_parcelas = int(input('Em quantas parcelas deseja dividir? '))
    parcela = valor_a_pagar / qtde_parcelas

    print(f'3x ou mais no cartão - Preço final: {valor_a_pagar:.2f}')
    print(f'O pagamento será em {qtde_parcelas}x de R${parcela:.2f}')

else:
    print('Opção de pagamento inválida. Escolha uma das 4 opções e digite o número da opção.')
