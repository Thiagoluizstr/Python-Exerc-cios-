'''
dados = list()
dados.append('Diego')
dados.append(25)
print(dados[0])

##############################

teste = list()
teste.append('Thiago')
teste.append(30)

galera = list()
galera.append(teste[:])
teste[0] = 'Cristina'
teste[1] = 51
galera.append(teste[:])

print(galera)

############################

galera = [['Thiago', 30], ['Luisa', 58], ['Diego', 7], ['Ana', 29]]
print(galera[0] [1])

for pessoa in galera:
    print(pessoa[1])

########################### '''
escreva = []
peso = []
maior = menor = 0

while True:
    escreva.append(str(input('Nome: ')))
    escreva.append(float(input('Peso: ')))

    if len(peso) == 0:
        maior = menor = escreva[1]
    else:
        if escreva[1] > maior:
            maior = escreva[1]
        if escreva[1] < menor:
            menor = escreva[1]

    peso.append(escreva[:])
    escreva.clear()
    continuar = str(input('Quer continuar [S/N] '))

    if continuar in 'Nn':
        break

print('-=' * 20)
print(f'Lista principal {peso}')
print(f'Ao todo, você cadastrou {len(peso)} pessoas')

print(f'O maior peso foi {maior}Kg. que é de ', end='')
for nome in peso:
    if nome[1] == maior:
        print(f'[{nome[0]}]', end='')
print()

print(f'O menor peso foi {menor}Kg. que é de ', end='')
for nome in peso:
    if nome[1] == menor:
        print(f'[{nome[0]}]', end='')
print()