# Programa que irá ler uma frase pelo teclado e mostre quantas vezes aparece a letra “A”
# Em que posição ela aparece a primeira vez 
# Em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece na {}º posição pela primeira vez'.format(frase.find('A') + 1))
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece na {}º posição'.format(frase.rfind('A') + 1))
