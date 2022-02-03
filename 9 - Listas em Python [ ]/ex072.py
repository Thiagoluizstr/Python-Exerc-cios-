numero = []
maior = 0
menor = 0

for cont in range(0, 5):
    numero.append(int(input(f'Digite uma valor para a posição {cont}: ')))

print(20*'-=-')

print(f'Voê digitou os valres {numero}')

print(f'O maior valor digitado foi {max(numero)} nas posições ', end=' ')
for i, v in enumerate(numero):
    if v == max(numero):
        print(f'{i}º...', end='')
print()

print(f'O menor valor digitado foi {min(numero)} nas posições', end=' ')
for i, v in enumerate(numero):
    if v == min(numero):
        print(f'{i}º...', end='')
print()

###############################################################################################

numero = []
maior = 0
menor = 0

for cont in range(0, 5):
    numero.append(int(input(f'Digite uma valor para a posição {cont}: '))) 

    if cont == 0:
        menor = menor = numero[cont]
    else:
        if numero[cont] > maior:
            maior = numero[cont]
        if numero[cont] < menor:
            menor = numero[cont]

print(20*'-=-')
print(f'Voê digitou os valres {numero}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')

for i, v in enumerate(numero):
    if v == maior:
        print(f'{i}º...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(numero):
    if v == menor:
        print(f'{i}º...', end='')
print()
