"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""
def ficha(n=None, g=None):
    """
    Mostra as informações do jogador(a).
    :param n: (Opcional) Nome do jogador(a)
    :param g: (Opcional) Quantidade de gols marcados pelo atleta.
    :return: Sem retorno
    """
    if n is None or n == '':
        n = '<desconhecido>'
    if g is None or g == '':
        g = 0

    print(f'{n} fez {g} gol(s) no campeonato.')

# Programa principal
print('=' * 30)
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)