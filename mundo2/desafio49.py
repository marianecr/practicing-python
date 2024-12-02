"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""
num = int(input('Digite o número para saber a tabuada dele: '))
print('='*20)
print(f'    TABUADA DE {num}')
print('='*20)
for i in range(1, 10):
    print(f'    {i} X {num} = ', i * num)