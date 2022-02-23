"""
Escreva um programa que receba 12 salários mensais, faça o somatório dos mesmos 
e apresente o total de salários recebidos no ano, o maior salário e o menor salário.
"""

def busca_maior_salario(lista_de_salarios):
	return max(lista_de_salarios)

def busca_menor_salario(lista_de_salarios):
	return min(lista_de_salarios)

def contabiliza_salario2():
	from operator import add
	from functools import reduce

	salario = []

	for _ in range(3):
		salario.append(int(input("Digite o salário: ")))

	soma_dos_salarios = reduce(add, salario)
	print("A soma dos sálarios é", soma_dos_salarios)
	print("O maximo sálario foi", busca_maior_salario(salario))
	print("O menor sálario foi", busca_menor_salario(salario))

def contabiliza_salario():
	i = 12     #12 é o número de vezes que irá repetrir
	soma = 0    #A soma inicia em 0 pois no while ela irá pegar os valores
	numero = []

	while i > 0:      #Enquanto o numero for maior que 0
		i = i - 1     #O numero será diminuido 1 de 12
		num = int(input("Digite o sálario:  "))       #Aqui serve para jogar os 12 numeros na tela
		soma = soma + num                            #Aqui ele faz a soma do valor inicial até os valores finais
		numero.append(num)

		
	print("A soma dos sálarios é", soma)
	print("O maximo sálario foi", busca_maior_salario(numero))
	print("O menor sálario foi", busca_menor_salario(numero))

if __name__ == '__main__':
	contabiliza_salario2()

