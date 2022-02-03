numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')

print('=' * 30)
print('   Trabalhando com tuplas  ')
print('=' * 30)

continuar = ' '

while continuar not in 'N':
    num = int(input('Digite um número entre 0 e 20: '))
    print('=' * 30)

    if 0 <= num <= 20:
        print(f'Você digitou o numero {numero[num]}')
        print('='*30)
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        print('=' * 30)

    if continuar == 'Ss':
        num = int(input('Digite um número entre 0 e 20: '))

    else:
        if continuar == 'Nn':
            break
print('FIM')

#######################################################

'''numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito',
          'dezenove', 'vinte')

n = -1

while n < 0 or n > 20:
    n = int(input('Digite um numero de 0 a 20: '))
print(f'Você digitou o numero {numero[n]}')'''





