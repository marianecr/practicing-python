"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""
# Desafio estendido com adição das outras categorias existentes atualmente

peso = float(input('Qual o peso da pessoa? '))
altura = float(input('Qual a altura da pessoa? '))
imc = peso / (altura ** 2)
print(f'O IMC é de {imc:.2f}.')
if imc <= 18.5:
    print('A pessoa está abaixo do peso.')
elif 18.5 < imc < 25:
    print('A pessoa está no peso ideal.')
elif 25 <= imc < 30:
    print('A pessoa está com sobrepeso.')
elif 30 <= imc < 35:
    print('A pessoa está com obesidade grau I.')
elif 35 <= imc < 40:
    print('A pessoa está com obesidade grau II.')
else:
    print('A pessoa está com obesidade grau III.')