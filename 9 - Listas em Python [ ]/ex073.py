valor = list()

while True:
    v = int(input('Digite um valor: '))

    if v not in valor:
        valor.append(v)
        print('Valor adicionado com sucesso...')
    else:
        if v in valor:
            print('Valor duplicado, não será adcionado!')
    seguir = str(input('Quer continuar? [S/N] '))

    if seguir in 'Nn':
        break

print('-=-' * 20)
valor.sort()
print(f'Você digitou os valores {valor}')