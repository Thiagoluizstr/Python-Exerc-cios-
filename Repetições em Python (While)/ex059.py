print('=='*10, 'Thiago Luiz', '=='*10)

sim = 'S'

total = cont = média = maior = menor = 0
while sim in 'Ss':

    numero = int(input('Digite um numero: '))
    total += numero
    cont += 1

    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    sim = str(input('Quer prosseguir: [s/n] '))

média = total / cont

print('Você digitou {} numeros e a média desses valores é {}'.format(cont, média))
print('O maior valor foi {} e o menor é {}'.format(maior, menor))


