"""
Programa de computador que mostra todas as características de um número
e junta informações dele. Recebendo o número: 
a. Informa se o número é positivo, negativo ou zero
b. Se for um número inteiro positivo, deves identificar se o mesmo é par ou ímpar
c. Caso seja ímpar, mostrar se é múltiplo de 3, múltiplo de 5 ou múltiplo de 7
"""

numero = (int(input('Digite um número inteiro: ')))

#Verificando se é positivo, negativo ou zero.
if numero > 0:
	print(" O numero", numero, "é positivo")
elif numero < 0:
	print(" O numero", numero, "é negativo")
elif numero == 0:
	print(" O numero é zero")

# Verificando se o numero é par ou impar.
if numero % 2 == 0:
	print(" O numero", numero, "é par")
else: 
	print(" O numero", numero, "é ímpar")
	if numero % 3 == 0:
		print(" É multiplo de 3")
	elif numero % 5 == 0:
		print(" É multiplo de 5")
	elif numero % 7 == 0:
		print(" É multiplo de 7")



	

