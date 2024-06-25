'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo1 + (10 - 1) * razao
termos = termo1
c = 0

print('Os 10 primeiros termos : \n')
while c < 10:
    print(f'{termos}', end=' - ')
    termos += razao
    c += 1
print('Fim')