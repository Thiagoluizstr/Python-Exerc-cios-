#Programa que leia o sexo de uma pessoa e só os valores 'M' e 'F'#

sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registro com sucesso'.format(sexo))
