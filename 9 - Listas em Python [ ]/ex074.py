lista = list()

for v in range(0, 5):
    valor = int(input('Digite um numero: '))

    if v == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'O valor {valor} foi adicionado na ultima posição...')
    else:
        c = 0
        while c < len(lista):
            if valor <= lista[c]:
                lista.insert(c, valor)
                print(f'O valor {valor} foi adicionado a posição {c}...')
                break
            c += 1

print(f'\nOs valores adicionados são {lista}')

