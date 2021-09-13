from time import sleep

print('=-='*5, 'Thiago Luiz', 5*'=-=')
print('programa desenvolvido "Menu de opções"')
print('=-='*14)

v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))

opção = 0

while opção != 5:
    print('[1] Somar ')
    print('[2] Multiplicar')
    print('[3] maior')
    print('[4] Novos valores')
    print('[5] Sair')
    opção = int(input('>>>> Qual é a sua opção?  '))
    print('=-'*16)

# Efetuando a soma entre os dois valores do menu
    if opção == 1:
        print('A soma entre {:.0f} e {:.0f} é {:.0f}'.format(v1, v2, (v1+v2)))
        print('=-' * 16)

# Efetuando a multiplicação entre os dois valores no menu
    elif opção == 2:
        print('A multiplicação entre {:.0f} e {:.0f} é {:.0f}'.format(v1, v2, (v1*v2)))
        print('=-' * 16)

# Mostrando o maior valor digitado
    elif opção == 3:
        if v1 < v2:
            print('O maior valor entre {:.0f} e {:.0f} é {:.0f}'.format(v1, v2, v2))
        if v2 < v1:
            print('O maior valor entre {:.0f} e {:.0f} é {:.0f}'.format(v1, v2, v1))
        else:
            print('Os valores {:.0f} e {:.0f} são iguais'.format(v1, v2))

# Novos numeros adicionados
    elif opção == 4:
        print('Informe os numeros novamente')
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))

# Encerramento do programa
    elif opção == 5:
        print('Aguardando', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)

# opção inválida no menu
    else:
        print('Opção inválida tente novamente')
print('FIM')







