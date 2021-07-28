#Programa que mostra na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep
for c in range(0, 52, 2):
    print(c, end=' ') # Adicionando o end='' a contagem é feita vertical #
    sleep(0.5)
print('Parabéns tarafe concluída com êxito!')