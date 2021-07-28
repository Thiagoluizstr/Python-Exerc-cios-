soma = 0
media = 0
maioridhomem = 0
nomevelho = ''
totamulher20 = 0

for p in range(1, 5):
    print('---- {}° PESSOAS ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridhomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridhomem:
        maioridhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totamulher20 += 1
media = soma / 4
print('A média do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totamulher20))