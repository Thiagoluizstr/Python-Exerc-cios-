numeros = (int(input('Digite o primeiro valor: ')),
           int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')),
           int(input('Digite o quarto valor: ')),
           int(input('Digite o quinto valor: ')))
print(f'Você digitou os valores {numeros} \n')


print(f'Quantas vezes o valor 9 apareceu {numeros.count(9)}')
if 3 in numeros:                                                                   # Se o 3 estiver dentro da tupla
    print(f'O numero 3 apareceu na posição {numeros.index(3) + 1}º')
else:                                                                              # Se não mostre a mensagem abaixo
    print(f'Não foi digitado o numero 3 em nenhuma posição')
print(f'Os valores pares digitados são', end=' ')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')