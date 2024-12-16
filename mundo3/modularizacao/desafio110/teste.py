import moeda
preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {(moeda.dobro(preco, True))}')
print(f'Aumento em 10%, fica em {moeda.aumentar(preco, 10, True)}')
print(f'Descontando 20%, fica em {moeda.diminuir(preco, 20, True)}')
