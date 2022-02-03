expressão = str(input('Digite uma expressão: '))

lista = []

for parentese in expressão:
    if parentese == '(':
        lista.append('(')
    elif parentese == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print(f'Sua expressão {expressão} está correta!')
else:
    print(f'Sua expressão {expressão} está errada!')