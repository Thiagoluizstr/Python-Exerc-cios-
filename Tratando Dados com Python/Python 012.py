print('Calculando desconto \n')

v = float(input('Digite o valor do produto: '))
d = v - (v * 5)/100
print('O valor do produto é R${} e com desconto de 5% sairá no valor de R${:.2f}'.format(v, d))