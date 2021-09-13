for c in range(0, 11):
    print(c)
print('Fim')

2 for c in range(1, 5):
    n = int(input('Digite o valor: '))
print('Fim')


c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

n = 1
while n != 0:  #Flag = ponto de parada#
    n = int(input('Digite um valor: '))
print('Fim')

s = 'S'
while s == 'S':
    n = int(input('Digite um valor: '))
    s = str(input('Quer continuar: [S/N]')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))