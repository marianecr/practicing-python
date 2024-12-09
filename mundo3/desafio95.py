"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
jogadores = list()
jogador = dict()
gols = list()

while True:
  jogador['nome'] = str(input('Nome do Jogador: ')).strip()
  partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

  for p in range(partidas):
    gols.append(int(input(f'Quantos gols na {p + 1}ª partida? ')))
  
  jogador['gols'] = gols[:]
  jogador['total'] = sum(gols)
  jogadores.append(jogador.copy())
  jogador.clear()
  gols.clear()

  resp = str(input('Deseja cadastrar mais um jogador [S/N]? ')).strip().upper()
  while resp not in 'SN':
    print('Opção inválida! Digite "S" para "SIM" ou "N" para "NÃO".')
    resp = str(input('Deseja cadastrar mais um jogador [S/N]? ')).strip().upper()
  
  if resp == 'N':
    break

print('=' * 35)
print(f'{"COD":<5} {"NOME":<8}  {"GOLS":<8} {"TOTAL":>10}')
print('-' * 35)

for pos, j in enumerate(jogadores):
  print(f'{pos:<5} {jogadores[pos]['nome']:<8}  {jogadores[pos]['gols']}   {jogadores[pos]['total']}')
print('-' * 35)

while True:
  resp2 = int(input('Mostrar levantamento de qual jogador (Digite o COD do jogador / 999 para sair)? '))
  if resp2 == 999:
    break
  
  if resp2 >= len(jogadores):
      print('Opção inválida! Não há jogador com esse código na lista. Digite um código válido.')
  else:
    print(f'--- LEVANTAMENTO DO JOGADOR {jogadores[resp2]['nome']}')
    
    for i, g in enumerate(jogadores[resp2]['gols']):
      print(f'  No jogo {i+1} marcou {g} gols.')
  
