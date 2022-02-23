""" 
Uma empresa paga a seus empregados um salário de R$ 500.00 por mês mais uma comissão de 5%
do valor da venda e um bônus que varia de acordo com a quantidade de produtos vendidos no mês. Se o vendedor conseguir
vender 5 produtos, ganha um bônus de R$ 1000.00; mas se o vendedor conseguir vender acima de 10 produtos, o bônus seria de
R$ 2500.00. Escreva um programa para calcular e imprimir o salário do vendedor num dado mês recebendo como dados de
entrada: (1) o nome do vendedor, (2) o número de produtos vendidos e (3) o valor total das vendas.
"""


nome_vendedor = (input(" Digite o nome do vendedor: "))

numero_produtos = (int(input(" Digite o numero de produtos: ")))

numero_vendas = (int(input(" Digite o numero de vendas: ")))


if numero_vendas < 5:                                     
	salario = (numero_vendas * 0.05) + 500                                # Se o numero de vendas for menor que 5, o valor total sera o salario mais a comissao de 5%.
	print(" Valor total das vendas : R$ ", salario)
elif numero_vendas >= 5 and numero_vendas < 10:                           # Se o numero for entre 5 e 10, ganhara o salario, comissao sobre o numero de vendas e o bonus de 1000.
	salario = (numero_vendas * 0.05) + 500 + 1000
	print(" Valor total das vendas : R$ ", salario)
elif numero_vendas >= 10:
	salario = (numero_vendas * 0.05) + 500 + 2500                         # Se o numero for maior ou igual a 10, ganhara o salario, comissao sobre o numero de vendas e o bonus de 2500.
	print(" Valor total das vendas: R$ ", salario)



print(" O vendedor " , nome_vendedor , "vendeu o total de " , numero_vendas , " produtos com o salario total de vendas em R$" , salario)






