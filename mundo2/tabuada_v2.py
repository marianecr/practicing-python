'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

numero = int(input('Digite um número inteiro qualquer: '))

print('¨' * 16)
print(f'  TABUADA DE {numero}')
print('¨' * 16)

for c in range(0, 10):
    print(f'  {numero} X {c} = ', numero * c)

print('¨' * 15)