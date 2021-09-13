print('Calculando Seno, Cosseno e Tangente de um angulo qualquer \n')

from math import sin,cos,tan
num = float(input('Digite um ângulo: '))
print('O SENO de {} é {:.2f}'.format(num, sin(num)))
print('O COSSENO de {} è {:.2f}'.format(num, cos(num)))
print('E a TANGENTE de {} é {:.2f}'.format(num, tan(num)))
