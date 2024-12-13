"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')"""
def leia_int(msg):
    okay = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            okay = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if okay:
            break

    return num

# Programa principal
n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}.')