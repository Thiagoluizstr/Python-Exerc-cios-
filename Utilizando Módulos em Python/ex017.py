print('Obtendo a medida do Cateto oposto e do Cateto adjacente, para calcular a Hipotenusa \n')

import math
co = float(input('Qual a medida do cateto opsto: '))
ca = float(input('Qual a medida do cateto adjacente: '))
hip = math.hypot(co, ca)
print('A Hipotenusa vai medir {:.2f}'.format(hip))