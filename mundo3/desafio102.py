"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: Número do qual será calculado o fatorial
    :param show: (Opcional). Booleano para mostrar ou não o cálculo do fatorial
    :return: Valor do fatorial de um número num.
    """
    fa = 1
    print('=' * 30)
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fa *= n

    return fa

# Programa principal
fat = fatorial(5, True)
print(fat)