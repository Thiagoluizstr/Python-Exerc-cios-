n = list()

while True:
    numero = int(input('Digite um valor: '))

    if numero not in n:
        n.append(numero)
        continuar = str(input('Quer continuar [S/N]: '))

    if continuar in 'Nn':
        break

n.sort(reverse=True)
print('-=-' * 20)
print(f'Você digitou {len(n)} numeros.')
print(f'Os valores em ordem decrescente são {n}')

if 5 in n:
    print('O valor 5 está na lista!')
else:
    if 5 not in n:
        print('O valor 5 não está na lista!')