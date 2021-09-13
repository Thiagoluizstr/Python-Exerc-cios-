print('Reajuste salarial')

s = float(input('Salário menssal: '))
r = s + (s * 15)/100
print('Seu salário é R${:.2f} e com um reajuste de 15% você passará a ganhar R${:.2f}'.format(s, r))