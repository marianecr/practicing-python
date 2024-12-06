"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
estudantes = []
aluno = []
resp = 0
while True:
  nome = str(input('Nome do estudante: ')).strip()
  nota1 = float(input('1ª nota: '))
  nota2 = float(input('2ª nota: '))
  media = (nota1 + nota2) / 2

  aluno.append(nome)
  aluno.append(nota1)
  aluno.append(nota2)
  aluno.append(media)
  estudantes.append(aluno[:])
  aluno.clear()

  resposta = str(input('Deseja inserir mais estudantes [S/N]? ')).strip().upper()

  if resposta == 'N':
    break

print('=' * 30)
print(f"{'ID'} {'NOME':<8}  {'MÉDIA':>12}")
print('-' * 30)

for e in estudantes:
  print(f"{estudantes.index(e)}  {e[0]:<8} {e[3]:>12.1f}")
print('-' * 40)

while True:
  resp = int(input('De qual estudante deseja ver as notas (Digite o ID do estudante / 999 para sair)? '))
  if resp == 999:
    break
  if resp <= len(estudantes) - 1:
    print(f'Notas de {estudantes[resp][0]}: {estudantes[resp][1]}, {estudantes[resp][2]}')