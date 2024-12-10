"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~ """
def escreva():
    mensagens = {'mensagem1': 'Python', 'mensagem2': 'Ciência de Dados é Legal', 'mensagem3': 'Fala, Mundo!'}
    for v in mensagens.values():
        print(f'{"="}' * (len(v) + 2))
        print(f' {v}')
        print('=' * (len(v) + 2))


escreva()