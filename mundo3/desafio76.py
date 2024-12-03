"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
produtos = (
    ("Capacete esportivo", 350.00),
    ("Jaqueta de couro", 600.00),
    ("Luvas de proteção", 120.00),
    ("Pneu traseiro 180/55", 700.00),
    ("Óleo para motor 10W-40", 60.00),
    ("Kit de relação", 450.00),
    ("Escapamento esportivo", 1200.00),
    ("Bateria selada 12V", 300.00),
    ("Protetor de tanque", 50.00),
    ("Bolsa de tanque", 200.00)
)

print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)

for prod in produtos:
  print(f'{prod[0]:.<30}', end='')
  print(f'R$ {prod[1]:>7.2f}')