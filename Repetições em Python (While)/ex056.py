print('='*8,'THIAGO LUIZ', '='*8)

print('=='*15)
print('Super progressão Aritimrética')
print('=='*15)

numero = int(input('Digite o 1º numero: '))
razão = int(input('Digite a razão: '))

cont = 1
termo = numero
mais = razão
total = 0
mais = 10

#Utilizando uma estrutura de repetiçao dentro de uma estrutura de repetição
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ➡ '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar: '))
print('FIM')




