"""
O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde (OMS) para dar uma
indicação sobre a condição de peso de uma pessoa adulta. 
O algoritimo utiliza o peso (kg) e a altura (m) de um adulto e apresenta a sua condição de
acordo com a Tabela de IMC. 
peso.
"""

sair = False
while sair == False:

	peso = float(input("Digite o peso:  "))  
	altura = float(input("Digite a altura:  "))  
	imc = ( peso / altura ** 2)
	print("O IMC é {:.2f}".format(imc))
	

	if imc <= 18.5:
		print("Condição: abaixo do peso")
	elif imc > 18.5 and peso <= 25:
		print("Condição: peso normal")
	elif imc > 25 and peso <= 30:
		print("Condição: acima do peso")
	elif imc > 30:
		print("Condição: obeso")


	exit = input("Deseja sair? (n/s):")
	if  == "s":
		sair = True

