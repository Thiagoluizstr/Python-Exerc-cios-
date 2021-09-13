'''print('Olá, me chamo Thiago Luiz.')
print('Sou formado em Eng. Elétrica com enfâse em Eletrônica')
print('Atualmente curso Ciência de Dados e Big Data Analytics')
print('Estou subindo alguns arquivos aqui no Github para mostrar meu aprendizado.')
print('Em breve estarei subindo alguns arquivos de projetos que estou trabalhando.')
print('Até breve.')'''


'pratica 1'

'''casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Salário de comprador? '))
tempo = int(input('Quanto anos de vinaciamento? '))

parcelas = casa / (tempo * 12)

print('O valor da casa é {} e você vai pagar em {} anos uma prestação de {:.2f}'.format(casa, tempo, parcelas))
if parcelas >= (salario * 30) / 100:
    print('Emprestimo NEGADO!')
    print('O valor excede 30% do seu salário')
else:
    print('Emprestimo APROVADO!')'''


'pratica 2'

'''print('CONVERSOR DE BASE NUMÉRICA')
print('--------------------------')
n = int(input('Digite um número: '))
print('--------------------------')
print('Escolha uma das opções de conversão')
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECINAL')
num = int(input('Qual a sua escolha: '))

if num == 1:
    print('O número {} em BINÁRIO é {}'.format(n, bin(n)))
elif num == 2:
    print('O número {} em OCTAL é {}'.format(n, oct(n)))
elif num == 3:
    print('O número {} em HEXADECIMAL é {}'.format(n, hex(n)))
else:
    print('Opção incorreta volte e escolha uma das 3 opções acima')'''

'partica 3'

'''n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

if n1 > n2:
    print('O numero {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('Os numeros são iguais')'''

'parte 4'

'''data = int(input('Ano de Nascimento: '))

alist = 2021 - data
falta = 18 - alist
passou = alist - 18

if alist == 18:
    print('Você tem {} anos e já pode se alistar'.format(alist))
elif alist > 18:
    print('Você tem {} anos deveria ter se alistado a {} anos'.format(alist, passou))
elif alist < 18:
    print('Você tem {} anos faltam {} anos para se alistar'.format(alist, falta))'''

'parte 5'

'''n1 = float(input('Nota do 1º Bimestre: '))
n2 = float(input('Nota do 2º Bemestre: '))

m = (n1 + n2) / 2

if m >= 7:
    print('Sua Média foi {}, APROVADO!'.format(m))
elif m < 4.9:
    print('Sua Média foi {} infelizmente, REPROVADO!'.format(m))
elif m >= 5 and m <=6.9:
    print('Sua Média foi {} precisa fazer RECUPERAÇÃO.'.format(m))'''

'parte 6'

'''from datetime import date

print('Vamos ver em qual clasificação você se encaixa')
data = int(input('Seu ano de nascimento: '))

atual = date.today().year
idade = atual - data

if idade <= 9:
    print('Você nasceu em {} e sua idade é {} anos, sua classificação é MIRIM'.format(data, idade))
elif idade >= 10 and idade <= 14:
    print('Você nasceu em {} e tem {} anos sua classificação é INFANTIL'.format(data, idade))
elif idade >= 15 and idade <= 19:
    print('Você nasceu em {] e tem {} anos sua classificação é JÚNIOR'.format(data, idade))
elif idade >= 20 and idade <= 25:
    print('Você nasceu em {} e sua idade é {} anos sua classificação é SÊNIOR'.format(data, idade))
elif idade > 25:
    print('Você naceu em {} e sua idade é {} anos sua classificaçõa é MASTER'.format(data, idade)) '''

print('Analisando o Triângulos parte II')
print('-----------------------------------')
n1 = float(input('Digite o valor de 1º seguimento: '))
n2 = float(input('Digite o valor do 2º seguimento: '))
n3 = float(input('Digite o valor do 3º seguimento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima podem formar uma TRIÂNGULO',end='')
    if n1 == n2 == n3:
        print(' EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('Os seguimento acima não podem formar um TRIÂNGULO')