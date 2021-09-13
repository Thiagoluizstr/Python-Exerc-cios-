soma = cont = 0

while True:

    numero = float(input('Digite um valor [999 para parar]: '))

    if numero == 999:
        break

    cont += 1

    soma += numero

print('A soma dos {} numeros é {:.0f}'.format(cont, soma))
