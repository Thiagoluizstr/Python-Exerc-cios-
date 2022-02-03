Tabela = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo',
          'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',
          'Athletico-PR', 'Cuiabá', 'Ceará', 'Atletico-GO',
          'São Paulo', 'Juventude', 'América-MG', 'Santos',
          'Bahia', 'Grêmio', 'Sport', 'Chapecoense')

print('=-='*13)
print(f'Lista de times do Campeonato Brasileiro: {Tabela}')
print('=-='*13)
print(f'Os 5 primeiros são: {Tabela[1:6]}')
print('=-='*13)
print(f'Os 4 ultimos são: {Tabela[-4:]}')
print('=-='*13)
print('Times em ordem alfábetica', sorted(Tabela))
print('=-='*13)
print(f'O lanterna da competição é a Chapecoense em {Tabela.index("Chapecoense")+1}ª lugar')