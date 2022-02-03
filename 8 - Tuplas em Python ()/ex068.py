from random import randint
print('O maior e o menor valor utilizando tuplas')

print('='*40)
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os cinco valores são: {n}')
print('='*40)

print(f'O maior valor é {max(n)}')
print('='*20)
print(f'O menor valor é {min(n)}')
print('='*20)