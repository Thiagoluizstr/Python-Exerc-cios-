maior = menor = total = cont = 0
produto = ' '

while True:
    print('-'*30)
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: R$ '))
    print('-'*30)

    cont += 1
    total += valor

    if valor > 1000:
        maior += 1
    else:
        if valor < 1000:
            menor += 1

    if cont == 1:
        menor = valor
        produto = nome
    else:
        if valor < menor:
            menor = valor
            produto = nome

    seguir = ' '
    while seguir not in 'SN':
        seguir = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if seguir == 'N':
        break

print('{:-^30}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total:.1f}')
print(f'Temos {maior} produtos acima de 1000 R$')
print(f'Temos {menor} produtos abaixo de 1000 R$')
print(f'O produto de menor preço custa {menor} que é {produto}')
