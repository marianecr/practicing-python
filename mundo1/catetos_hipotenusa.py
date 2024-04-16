'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import sqrt

cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = sqrt(pow(cat_oposto,2) + pow(cat_adjacente,2))

print(f'Com os cateto oposto e adjecente de comprimentos {cat_oposto :.2f} e {cat_adjacente :.2f}, respectivamente, o comprimento da ipotenusa será de {hipotenusa :.2f}, aproximadamente.')

