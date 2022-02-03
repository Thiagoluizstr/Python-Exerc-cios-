lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche) #mostrará todos os elementos da tupla

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[:2]) #mostraŕa o elemento 0º até o 1º elemento desconsiderando o 2º elemento

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-1]) #mostrará de trás para frente iniciando pelo o ultimo elemento da tupla

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2:]) #iniciará do penultimo elemento e vai até o final da tupla de trás para frente

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1:3]) #vai escrever do 1º elemento ao 3º elemento, porém só mostrará até o 2º elemento da tupla pelo fatiamento

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:]) #mostrará do 2º elemento até o ultimo elemento da tupla

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[2:]) #mostrará do 2º elemento até o ultimo elemento da tupla

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Três maneiras diferentes de fazer a mesma coisa usando "for" #

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'eu vou comer {comida}')
print('Comi de mais !')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

lanche = ('Hambueguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # A função "sorted" organiza por ordem alfabética

# A ordem nas tuplas não equivale como na matemática
a = (2, 5, 4)
b = (1, 3, 6)

#Essa função irá juntar as tuplas e não irá somar
c = a + b

# Utilizando a função "len" irá mostrar o total de elementos da tupla.
# Utilizando a função "(c.count(obj))" irá mostrar quantas vezes aparec um objeto na tupla.
# Utilizando a função "(c.index(obj))" irá mostrar a posição do objeto na tupla mostrando a 1º ocorrência em caso de repetição.
# Para ver o 2º objeto é só utilizar a mesma função "(c.index(obj, obj))" e expecíficar para iniciar a contagem do 2º obj chamado de deslocamento
print(c)

pessoa = ('Thiago', 30, 'M', 105.40)
del(pessoa) # A função "del" pode apagar uma tupla inteira, porém não pode apagar apenas 1 objeto da tupla.
print(pessoa)