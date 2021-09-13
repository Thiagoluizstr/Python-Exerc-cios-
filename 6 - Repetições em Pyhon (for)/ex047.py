f = str(input('Digite uma frase: ')).strip().upper()

p = f.split()
j = ''.join(p)
inv = ''

for l in range(len(j) - 1, -1, -1):
    inv += j[l]
if inv == j:
    print('Sua frase de trás pra frente é {}'.format(j, inv))
    print('Sua frase é um PALÍNDROMO', end=' ')
else:
    print('Sua frase de trás para frente é {}'.format(j, inv))
    print('Sua frase não é um PALÍNDROMO')
