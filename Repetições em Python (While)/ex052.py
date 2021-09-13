from random import randint
computador = randint(0, 10)

print('O computador está pensando... Pronto acabei de pensar em um numero de 0 a 10.')
print('Tenta adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tenta mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))



