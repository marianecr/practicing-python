"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Flamengo."""

times = ('Botafogo', 'Palmeira', 'Flamengo', 'Internacional', 'Fortaleza', 'São Paulo', 'Bahia', 'Corinthians', 'Cruzeiro', 'Vitória', 'Grêmio', 'Vasco', 'Atlético-MG', 'Athletico-PR', 'Juventude', 'Fluminense', 'Criciúma', 'Bragantino', 'Cuiabá', 'Atlético-GO')

print(f'Os times da séria A do Brasileirão 2024: {times}.')
print('-' * 30)
print(f'Os 5 primeiros colocados são: {times[:6]}.')
print('-' * 30)
print(f'Os últimos 4 colocados são: {times[-4:]}.')
print('-' * 30)
print(f'Times em ordem alfabética: {sorted(times)}.')
print('-' * 30)
print(f'O Flamengo está na posição {times.index('Flamengo') + 1}ª posição.')