'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
opcao = 0

while opcao != 5:
    opcao = int(input('''Qual operação deseja realizar? 
        [1] - Somar
        [2] - Multiplicar
        [3] - Maior
        [4] - Inserir novos números
        [5] - Sair do programa
        >>> '''))
    
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é igual a {soma}.')
        
    elif opcao == 2:
        multi = num1 * num1
        print(f'{num1} vezes {num2} é igual a {multi}.')
    
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print(f'O maior valor é {maior}.')
        elif num2 > num1:
            maior = num2
            print(f'O maior valor é {maior}.')
        else:
            print('Os dois valores são iguais.')
        
    elif opcao == 4:
        num1 = float(input('Digite o novo valor: '))
        num2 = float(input('Digite o outro novo valor: '))
    
    elif opcao == 5:
        break
    
    else:
        print('Opção inválida. Por favor, selecione uma das opções apresentadas.')