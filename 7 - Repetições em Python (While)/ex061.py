while True:
    numero = int(input('Quer ver qual tabuada, digite um numero: '))
    if numero < 0:
        break
    print('=' * 30)
    for cont in range(0, 11):
        print('{} x {} = {}'.format(numero, cont, numero*cont))
    print('=' * 30)
print('FIM')



