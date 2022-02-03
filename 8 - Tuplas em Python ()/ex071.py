lista = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRTICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO',)

for palavra in lista:
    print(f'\nNa palavara {palavra} temos ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')




