# Programa que irá ler o nome completo de uma pessoa, 
# E Mostrará em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print('Olá serja bem vindo !')
print('Seu primeiro nome {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
