from datetime import date
atual = date.today().year

for pess in range(0, 7):
    ano = int(input('Digite sua data de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        print('Você tem {} anos e já é maior de idade'.format(idade))
    if idade <= 0:
        print('Você ainda não nasceu e tem zero anos')
    else:
        print('Você tem {} anos e ainda é menor idade'.format(idade))


