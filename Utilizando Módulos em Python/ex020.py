print('Escolha uma ordem na lsita \n')

from random import shuffle

a1 = str(input('Digite o 1ª nome: '))
a2 = str(input('Digite o 2ª nome: '))
a3 = str(input('Digite o 3ª nome: '))
a4 = str(input('Digite 0 4º nome: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print(lista)

