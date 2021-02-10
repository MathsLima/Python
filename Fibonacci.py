"""
Os números de Fibonacci são uma sequência de inteiros onde cada um é igual à soma dos dois anteriores, e os dois primeiros números são 1 e 1. 
Por exemplo, eis alguns números dessa sequência: 1, 1, 2, 3, 5, 8, 13, 21, … 
O programa é capaz de calcular e exibir os números de Fibonacci menores ou iguais a 1000. 
"""

fa = 1
f = 1

print(f)
while (f <= 1000):
	print(f)
	fa,f = f, f + fa
