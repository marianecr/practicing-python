"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

salario_atual = float(input('Digite o salário atual do colaborador: R$'))

novo_salario = salario_atual + (salario_atual * 0.15)

print(f'Com o reajuste de 15%, o salário passará de R${salario_atual:.2f} para R${novo_salario:.2f}.')
