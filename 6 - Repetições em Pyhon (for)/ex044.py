print('Programa que leia apenas numeros interiros e mostre a soma dos numero pares apenas')
soma = 0
cont = 0
for p in range(1, 7):
    n = int(input('Digte o {}º numero: '.format(p)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} pares e a soma entre os numeros é {}'.format(cont, soma))0