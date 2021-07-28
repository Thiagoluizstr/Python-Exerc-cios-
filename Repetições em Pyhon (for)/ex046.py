n = int(input('Digite um numero: '))
tot = 0
for t in range(1, n + 1):
    if n % t == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(t), end='')
print('\n\033[mO numero {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Ele não é PRIMO')


