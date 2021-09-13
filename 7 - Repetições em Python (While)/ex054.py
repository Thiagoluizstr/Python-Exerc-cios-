from time import sleep

print('Calcular fatorial de um numero')
n = int(input('Digite um numero: '))

contador = n
f = 1

print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end=' ')
    sleep(1)
    print(' x ' if contador > 1 else ' = ', end='')
    sleep(1)
    f *= contador
    contador -= 1
print('{}'.format(f))
sleep(1)






