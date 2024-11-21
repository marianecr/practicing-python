'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input('Insira um número inteiro qualquer: '))

opcao = int(input('''Escolha a opção de conversão de base:
      1) BINÁRIO
      2) OCTAL
      3) EXADECIMAL
      '''))

if opcao == 1:
    print(f'{numero} na forma binária é {bin(numero)[2:]}.')

elif opcao == 2:
    print(f'{numero} na base octal é {oct(numero)[2:]}.')

elif opcao == 3:
    print(f'{numero} na forma hexadecimal é {hex(numero)[2:]}.')

else:
    print('O número que você digitou não corresponde a uma opção válida. Por favor, escolha entre 1, 2 ou 3.')
