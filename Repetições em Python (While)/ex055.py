print('='*25)
print(' Progressão Aritimética ')
print('='*25)

numero = int(input('Primeiro numero: '))
razão = int(input('Razão no numero: '))

cont = 1
termo = numero

while cont <= 10:
    print('{} ➡ '.format(termo), end=' ')
    termo += razão
    cont += 1
print('Fim')
