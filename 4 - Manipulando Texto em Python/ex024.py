# programa que le o nome de uma cidade diga se ela começa ou não com o nome “RIO”.

cid = str(input('Digite o nome da cidade? ')).strip()
print(cid[0:3].upper() == 'RIO')