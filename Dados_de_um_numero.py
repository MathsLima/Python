"""
Programa que lê um número não determinado de valores e calcule a média
aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
negativos e o percentual de valores negativos e positivos. A leitura deve parar quando o número
informado for 9999.
"""
num = int(input("Digite um numero: ")) 

soma = 0
qnt = 0
qnt_pos = 0
qnt_neg = 0

while (num != 9999):
	soma = soma + num
	qnt = qnt + 1
	if num >= 0:
		qnt_pos = qnt_pos + 1
	else:
		qnt_neg = qnt_neg + 1
	num = int(input("Digite um numero: "))

media = soma / qnt
per_pos = (qnt_pos / qnt) * 100
per_neg = (qnt_neg / qnt) * 100


print( " A média dos valores lidos", media)
print( " A qnt de valores positivos", qnt_pos)
print( " A qnt de valores negativos", qnt_neg)
print( " percentual de valores positivos", per_pos, "%")
print( " percentual de valores negativos", per_neg, "%")


