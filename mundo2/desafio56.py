"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
soma = 0
menos_20 = 0
mulheres = 0
idade_mais_velho = 0
nome_mais_velho = ''
total_fluidos = 0

for i in range(1, 5):
    print(f'=== {i}ª PESSOA ===')
    nome = str(input(f'Digite o nome: ')).strip()
    idade = int(input('Digite a idade:'))
    genero = str(input('Digite o gênero (F para feminino / M para masculino / O para flúido|não binário): ')).strip().upper()

    soma += idade

    if genero == 'F':
        mulheres += 1

    if genero == 'O':
        total_fluidos += 1

    if genero == 'F' and idade < 20:
        menos_20 += 1

    if i == 1 and genero == 'M': # Se a primeira pessoa for homem, já entra como o mais velho
        idade_mais_velho = idade
        nome_mais_velho = nome

    if genero == 'M' and idade > idade_mais_velho: # Se a primeira pessoa não for homem ou outro homem aparecer e for mais velho
        idade_mais_velho = idade
        nome_mais_velho = nome

media = soma / 4
print(f'A média de idade do grupo é de {media:.0f} anos.')
print(f'O grupo possui {mulheres} mulheres e {menos_20} possuem menos de 20 anos .')
print(f'O homem mais velho se chama {nome_mais_velho} e possui {idade_mais_velho} anos.')
print(f'{total_fluidos} pessoas do grupo possuem gênero flúido ou não binário 🏳️‍🌈.')