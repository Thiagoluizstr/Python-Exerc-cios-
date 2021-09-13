print('Locadora de carros \n ')
km = float(input('Quantos quilometros percorreu: '))
d = float(input('Quandos dias ficou com o carro: '))
k = km * 0.15
d1 = d * 60
t = d1 + k
print('Então percorreu km{} e ficou {} dias com o carro, sendo assim o total pagar será {}'.format(km, d, t))