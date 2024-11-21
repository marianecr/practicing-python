preco = float(input('Insira o preço do produto: R$'))
opcao_pagamento = int(input('''Qual a forma de pagamento você deseja: 
                            1 - À VISTA COM DINHEIRO / CHEQUE (10% DE DESCONTO)
                            2 - À VISTA NO CARTÃO (5% DE DESCONTO)
                            3 - ATÉ 2X NO CARTÃO (SEM DESCONTO)
                            4 - 3X OU MAIS VEZES NO CARTÃO (20% DE JUROS)
                            >>> '''))

match opcao_pagamento:
    case 1:
        valor_a_pagar = preco - (preco * 0.1)
        print(f'À vista com dinheiro / cheque - Preço final: R${valor_a_pagar:.2f}')
    
    case 2:
        valor_a_pagar = preco - (preco * 0.05)
        print(f'À vista no cartão - Preço final: R${valor_a_pagar:.2f}')

    case 3:
        print(f'Até 2x no cartão - Preço final: R${preco:.2f}')
    
    case 4:
        valor_a_pagar = preco + (preco * 0.2)
        qtde_parcelas = int(input('Em quantas parcelas deseja dividir? '))
        parcela = valor_a_pagar / qtde_parcelas

        print(f'3x ou mais no cartão - Preço final: {valor_a_pagar:.2f}')
        print(f'O pagamento será em {qtde_parcelas}x de R${parcela:.2f}')
    
    case _:
        print('Opção de pagamento inválida. Escolha uma das 4 opções e digite o número da opção.')