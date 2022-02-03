lista = (print('____________________________________________'),
         print('             LISTA DE PREÇOS                '),
         print('____________________________________________'),
         print('Lápis..............................R$   1.75'),
         print('Borracha...........................R$   2.00'),
         print('Caderno............................R$  15.90'),
         print('Estojo.............................R$  25.00'),
         print('Transferidor.......................R$   4.20'),
         print('Compasso...........................R$   9.99'),
         print('Mochila............................R$ 120.32'),
         print('Canetas............................R$  22.30'),
         print('Livro..............................R$  34.90'),
         print('____________________________________________ \n'))


#Segunda forma de fazer a lista formato tabular#

tabela = (print('''____________________________________________
              LISTA DE PREÇOS
____________________________________________
Lápis..............................R$   1.75
Borracha...........................R$   2.00
Caderno............................R$  15.90
Estojo.............................R$  25.00
Transferidor.......................R$   4.20
Compasso...........................R$   9.99
Mochila............................R$ 120.32
Canetas............................R$  22.30
Livro..............................R$  34.90
____________________________________________ \n'''))


#Terceira forma de fazer uma lista formatada#

listagem = ('Lápis', 1.75,
            'Borracha',  2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90,)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*40)
for pos in range(0, len(listagem)): #
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_'*40)