"""
A fim de agilizar o tratamento para os pacientes que apresentavam algum risco no hospital. A tarefa consiste em classificar
um paciente em um dos 3 grupos de riscos: alto risco, médio risco ou baixo risco, dependendo de suas
características, onde cada característica equivale a uma pontuação. O programa que recebe
como entrada a idade de uma pessoa e identifique se esta é uma criança (idade entre 0 e 11 anos) e que corresponde a 2
pontos, adolescente (entre 12 e 17 anos) e que corresponde a 2 pontos, adulto (entre 18 e 60 anos) e que corresponde a 3
pontos, ou idoso (idade maior que 60 anos) e que corresponde a 6 pontos. Além dessa informação, você deve perguntar ao
paciente (1) se ele tem alguma doença respiratória pré-existente? Se sim, corresponde a 3 pontos; (2) se o paciente é obeso?
Se sim, corresponde a 2 pontos; e (3) se o paciente apresenta diabetes? Se sim, corresponde a 2 pontos. No final, deve-se
somar a pontuação alcançada, e se ficar abaixo de 4 pontos esse paciente apresenta baixo risco; entre 4 e 5 pontos, o
paciente apresenta médio risco; e se a pontuação for igual ou superior a 6 pontos, esse paciente apresenta alto risco. Alguns
exemplos de saída do seu programa é apresentado abaixo:
a. O paciente é adolescente e apresenta médio risco. (Perfil de entrada: 15 anos e obeso)
b. O paciente é idoso e apresenta alto risco. (Perfil de entrada: 65 anos sem problemas pré-existentes)
"""
idade = int(input("Digite a idade do paciente: "))

#classificação
if idade <= 11:
	classificacao = "criança"
	pontuação = 2
elif idade < 18:
	classificacao = "adolescente"
	pontuação = 2
elif idade <= 60:
	classificacao = "adulto"
	pontuação = 3
else:
	classificacao = "idoso"
	pontuação = 6

#perguntas
doenca = input("O paciente possui doença respiratória pré-existente? (SIM ou NAO) ")
if doenca == "SIM":
	pontuação = pontuação + 3

obeso = input("O paciente é obeso? (SIM ou NAO) ")
if obeso == "SIM":
	pontuação = pontuação + 2

diabete = input("O paciente possui diabetes? (SIM ou NAO) ")
if diabete == "SIM":
	pontuação = pontuação + 2

#risco
if pontuação < 4:
	risco = "baixo"
elif pontuação == 4 or pontuação == 5:
	risco = "médio"
else:
	risco = "alto"

print( " O paciente é", classificacao, " e apresenta", risco, "risco")