# Programa que leia o nome completo de uma pessoa e mostre:

# Em letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

n = str(input('Digite nome: ')).strip()

print('Analisando seu nome...')
print('Seu nome em Maiúsculo {}'.format(n.upper()))
print('Seu nome em Minúsculo {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras '.format(n.find(' ')))

# Segunda forma de resolução utilizando "split" 

n = str(input('\n Digite seu nome: '))
div = n.split()

print('Seu nome todo em Maiúsculo é {}'.format(n.upper()))
print('Seu nome todo em Minúsculo é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(div[0], len(div[0]))) 