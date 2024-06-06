'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

altura = float(input('Digite a altura da pessoa (m): '))
peso = float(input('Digite o peso da pessoa (kg): '))

imc = peso / (altura ** 2)

print(f'O IMC da pessoa é {imc:.1f}.')

if imc < 18.5:
    print('A pessoa está abaixo do peso ideal.')

elif imc >= 18.5 and imc <= 25:
    print('A pessoa está no peso ideal.')

elif imc > 25 and imc <= 30:
    print('A pessoa está com sobrepeso.')

elif imc > 30 and imc <= 40:
    print('A pessoa está com obesidade.')

else:
    print('A pessoa está com obesidade mórbida.')