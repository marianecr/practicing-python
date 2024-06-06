'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento da pessoa atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print(f'A pessoa atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria de competição: MIRIM')
elif idade <= 14:
    print('Categoria de competição: INFANTIL')
elif idade <= 19:
    print('Categoria de competição: JÚNIOR')
elif idade <= 25:    
    print('Categoria de competição: SÊNIOR')
else:
    print('Categoria de competição: MASTER')
