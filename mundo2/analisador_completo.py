''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''

soma = 0
maiorIdadeHomem = 0
nomeMaisVelho = 0
totalIdadeM20 = 0
totalFluido = 0

for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    genero = str(input(f'Digite o gênero da {c}ª pessoa [M para Masculino] - [F para Feminino] - [FL para Fluido]: ')).strip().upper()

    soma += idade

    if c == 1 and genero == 'M':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if genero == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if genero == 'F' and idade < 20:
        totalIdadeM20 += 1
    if genero == 'FL':
        totalFluido += 1

media = soma / 4
print(f'''A média de idade das pessoas do grupo é de {media:.1f}.
O homem mais velho se chama {nomeMaisVelho} e ele possui {maiorIdadeHomem} anos.
Há {totalIdadeM20} mulheres com menos de 20 anos.
Há {totalFluido} pessoas de gênero fluido.''')
