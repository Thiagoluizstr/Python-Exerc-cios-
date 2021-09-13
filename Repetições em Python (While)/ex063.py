print('-'*5,'THIAGO LUIZ', 5*'-')

total = masculino = mulher = 0

while True:
    print('-' * 25)
    print('  CADASTRE UMA PESSOA ')
    print('-' * 25)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    seguir = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if sexo == 'M':
        masculino += 1

    if sexo == 'F':
        if idade < 20:
            mulher += 1

    if idade > 18:
        total += 1

    if seguir == 'N':
        print(f'Quantas pessoas tem mais de 18 anos: {total}')
        print(f'Quantos homens foram cadastrados {masculino}')
        print(f'Quantas mulheres tem menos de 20 anos: {mulher}')
        break
print('FIM')






