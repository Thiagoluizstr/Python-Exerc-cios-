print('='*25)
print('  10 TERMOS DE UMA PA ')
print('='*25)

p = int(input('Primeiro numero: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r

for c in range(0, d + r, r):
    print('{}'.format(c), end=' ➡ ')
print('Terminou!')


