# Programa que leia o nome de uma pessoa e diga se ela tem “Luiz” no nome.

n = str(input('Digite seu nome? ')).strip()
print('Realmente seu nome Luiz? {}'.format('luiz' in n.lower()))
