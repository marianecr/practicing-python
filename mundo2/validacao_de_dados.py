'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

genero = str(input('Digite o gênero da pessoa [F - Feminino; M - Masculino; N - Não binário ou Fluido]: ')).strip().upper()[0]

while genero not in 'FMN':
    genero = str(input('Essa opção não consta. Por favor, digite uma das letras correspondentes ao gênero da pessoa [F - Feminino; M - Masculino; N - Não binário ou Fluido]: ')).strip().upper()[0]

print('Obrigada!')
