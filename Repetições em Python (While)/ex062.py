from random import randint

print('----THIAGO LUIZ----')
print('==== PAR OU ÍMPAR? ====')

v = 0
#Estrutura de repetição
while True:
    num = int(input('Escolha um numero: '))
    maquina = randint(0, 21)
    total = num + maquina
    escolha = ' '

#Estrutura de repetição dentro de outra estrutura de repetição
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {num} e maquina {maquina} o total é {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

#Estrutura de Condição
    if escolha == 'P':

        #Estrutura de Condição aninhada
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

#Estrutura de Condição
    elif escolha == 'I':

        #Estrutura de Condição aninhada
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break #Essa instrução oferece a possibilidade de sair de um loop quando uma condição externa é acionada.

    print('Vamos jogar de novo...')
print(f'FIM DE JOGO! Você ganhou {v} vez')