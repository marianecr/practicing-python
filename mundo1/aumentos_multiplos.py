'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input('Difite o valor do salário do funcionário: R$'))

if salario <= 1250:
    novo_salario = (salario * 0.15) + salario
else:
    novo_salario = (salario * 0.1) + salario

print(f'Tendo um salário atual de R${salario:.2f}, seu salário passará para R${novo_salario:.2f}.')
