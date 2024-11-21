"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

from math import sin, cos, tan, pi

angulo = float(input('Digite o valor do ângulo em graus: '))

angulo_radiano = (angulo * pi) / 180

print(f'Os seno, cosseno e tangente de {angulo}° é {sin(angulo_radiano):.2f}, {cos(angulo_radiano):.2f} e {tan(angulo_radiano):.2f}, respectivamente.')