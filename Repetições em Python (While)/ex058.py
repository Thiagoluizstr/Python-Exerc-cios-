numero = int(input('Digite um número [999 para parar]: '))

cont = 0
soma = 0

while numero != 999:
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))