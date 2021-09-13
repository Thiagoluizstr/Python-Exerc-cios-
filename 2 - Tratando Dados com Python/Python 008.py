print('Programa de conversão de medidas')

m = float(input('Digite a medida ? '))
c = (m * 100)
m1 = (m * 1000)
print('O valor de {:2} m em milímetros é {:2}mm e em centimetros é {}cm '.format(m, m1, c))