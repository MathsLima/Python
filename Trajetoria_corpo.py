"""
A trajetória de um projétil disparado com certa velocidade e determinado ângulo em relação ao solo pode ser calculada através da seguinte fórmula:
"""

from math import radians, tan, cos

g = 9.81

v0 = float(input("Digite a velocidade inicial: "))
ang = float(input("Digite o angulo inicial: "))
y0 = float(input("Digite a altura inicial: "))

ar = radians(ang)

y = y0 
x = 0

while(y > 0):
	y = (x * tan(ar)) - (1/(2*v0**2)) * ((g*x**2)/cos(ar)**2) + y0
	print("{:.2f}".format(x), "\t", "{:.2f}".format(y))
	x= x + 1


# Este exercicio irá mostrar o quanto um objeto sobre e desce atraves da lei da fisica.