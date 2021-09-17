print('='*30)
print('{:^30}'.format('BANCO LIMA'))
print('='*30)

valor = int(input('Valor do saque: R$ '))
total = valor
cédula = 100
cétotal = 0

while True:
    if total >= cédula:
        total -= cédula
        cétotal += 1
    else:
        print(f'Total de {cétotal} cédulas de R${cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        cétotal = 0
        if total == 0:
            break

