"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""
pesos = []
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}ª: '))
    pesos.append(peso)
print(f'O maior peso foi de {max(pesos)} kg e o menor foi {min(pesos)} kg.')
