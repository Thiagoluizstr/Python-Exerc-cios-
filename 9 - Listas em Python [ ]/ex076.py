lista = []
par = []
impar = []

while True:

    numero = int(input('Digite um numero: '))
    continuar = str(input('Deseja continuar [S/N]: '))
    lista.append(numero)

    if continuar in 'Nn':
        break
print(f'\nOs valores digitados na lista foram {lista}')

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'Os valores pares da lista foram {par}')
print(f'Os valores impares da lista foram {impar}')