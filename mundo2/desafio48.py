"""Faça um programa que calcule a soma entre todos os números ÍMPARES que são múltiplos de três e que se encontram no intervalo de 1 até 500."""
soma = 0
count = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        count += 1
print(f'A soma dos {count} múltiplos de 3 entre 1 e 500 é igual a {soma}.')