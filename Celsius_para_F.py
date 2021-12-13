"""
Programa para exibie, em uma tabela, as temperaturas de 0 a 100 Celsius convertidas para Fahrenheit. 
"""
print("Celsius \t Fahrenheit")

c = 0
while (c < 101):
	f = c * (9/5) + 32
	print(c,"\t", "{:.1f}".format(f))
	c = c + 1
