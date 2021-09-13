print('Programa que mostra a tabuada que o usuário escolher')
print('-=-'*13)

num = int(input('Digite um número que farei a tabuada: '))
for t in range(1, 11):
    print('{} x {:2} = {}'.format(num, t, num*t))