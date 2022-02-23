"""
Você gostaria de fazer uma previsão de quanto será o seu grau final em uma disciplina. O programa informa a nota que
você acredita que terá ou tem nos trabalhos da disciplina, e informa se você passou direto, se ficou em recuperação ou se 
foi reprovado direto. Se a previsão for ter entrado em recuperação, você deve informar qual a nota que acredita que pode tirar 
na avaliação final.

Por fim, você gostaria de comparar a sua nota final na disciplina com outras universidades que apresentam o conceito, como indicado abaixo.
a. Média final entre 0 e 4 (inclusive, inclusive) conceito D
b. Média final entre 4 e 6 (exclusive, inclusive) conceito C
c. Média final entre 6 e 8 (exclusive, inclusive) conceito B
d. Média final entre 8 e 10 (exclusive, inclusive) conceito A
Neste sentido, a saída do seu programa deve informar tanto a sua nota final, como o conceito correspondente.
"""

Aluno = print(input("Nome do Aluno: "))

T1 = (float(input("Digite a nota T1: " )))
T2 = (float(input("Digite a nota T2: " )))
T3 = (float(input("Digite a nota T3: " )))
TF = (float(input("Digite a nota do trabalho final TF: ")))

#Calculo para G1
G1 = (((2 * T1) + (2 * T2) + (2 * T3) + (4 * TF)) / 10)

#Aluno reprovado direto
if G1>= 0 and G1 < 4:
	print("Aluno reprovado")
	print(" Média =", G1)

#Aluno aprovado direto
if G1 >= 7:
	print(" Aluno aprovado")
	print(" Média =", G1)

#Aluno em G2
if G1 > 4 and G1 < 7:
	print( "Aluno em G2")
	print(" Média =", G1)

	pergunta = input("Aluno em G2: Deseja calcular a nota mímina de avaliação final? (sim ou nao)")
	if  (pergunta == "sim"):
		Nota_final = 10 - G1
		print(" A nota final para obter aprovação é", Nota_final)
	if (pergunta == "nao"):
		print("Bye!")

if G1 <= 0 and G1 < 4:
	print(" Conceito D")
if G1 >= 4 and G1 < 6:
	print(" Conceito C")
if G1 >= 6 and G1 < 8:
	print(" Conceito B")
if G1 >= 8 and G1 <= 10:
	print(" Conceito A")







