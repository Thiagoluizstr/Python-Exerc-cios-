print('Programa leia o peso de cinco pessoas. Nofinal mostre o maior e menor peso')
print('-='*38)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o {}º peso da pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
