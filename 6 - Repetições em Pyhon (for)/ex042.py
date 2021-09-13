soma = 0 # Iníciando com um acumulador

cont = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        soma = soma + m
        cont = cont + 1
    print(m)
print('A soma entre todos os {} valores que são múltiplos de  três {}'.format(cont, soma))