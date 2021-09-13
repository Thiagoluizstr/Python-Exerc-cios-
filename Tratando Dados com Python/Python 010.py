print('Conversor de moedas')

real = float(input('Digite o valor ? R$ '))
d = real / 5.38
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, d))