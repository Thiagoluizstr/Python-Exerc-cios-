from time import sleep

print('='*30)
print('{:^30}'.format('BANCO lIMA'))
print('='*30)


while True:
    print('Cédulas disponivés no momento')
    sleep(1)
    print('[R$ 5] [R$ 10]')
    print('[R$ 20] [R$ 50]')
    print('[R$ 100] [R$ 200]')

    operação = ' '
    valor = 0
    while operação not in 'N':
        print('=' * 30)
        valor = float(input('Que valor deseja sacar? R$ '))
        if valor == 5:
            print('Aquarde um momento', end='')
            sleep(1)
            print('.', end='')
            sleep(1)
            print('.', end='')
            sleep(1)
            print('.', end='')
            sleep(1)
            print('.')
            sleep(1)
            print('Pode Retirar o dinheiro')

        operação = str(input('Deseja seguir com a operção: [S/N] ')).strip().upper()[0]
        sleep(1)

    print('FIM DA OPERAÇÃO')
    print('Obrigado e volte sempre')
    break

