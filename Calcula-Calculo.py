
print('Calcula - Calculo')
print('Digite o primeiro numero: ')
nUm = int(input())
print('Digite o segundo numero: ')
nDois = int(input())
aDici = 1
sUB = 2
mUlt = 3
print('Escolha um operador: + = 1 , - = 2 , * = 3')
operador = int(input())
if operador == aDici :
 soma = nUm + nDois
 print ("{0} + {1} = {2}".format(nUm, nDois, soma))
elif operador == sUB:
  soma = nUm - nDois
  print ("{0} - {1} = {2}".format(nUm, nDois , soma))
elif operador == mUlt:
  soma = nUm * nDois
  print("{0} * {1} = {2}".format(nUm,nDois,soma))
else:
  print('Erro incomun!!')

