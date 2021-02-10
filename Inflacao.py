"""
Algoritimo de inflação com reajuste de preço.

Com o novo preço, o produto troca de categoria e para qual vai, uma vez que cada categoria tem um selo diferente. As categorias são:
a. Selo Azul = R$ 0.01 a R$ 50.00
b. Selo Verde = R$ 50.01 a R$ 99.99
c. Selo Amarelo = R$ 100.00 a R$ 199.99
d. Selo Vermelho = Maior que R$ 200.00
"""

preco_antigo = (float(input(" Preço Antigo: R$ ")))

if preco_antigo < 100:                                     # Condição para o preço antigo.
	preco_novo = (preco_antigo * 0.1) + preco_antigo       # Foi criado uma variavel para poder utlizar no calculo e nas condicoes de selo com o nome de preço novo
	print(" Preço novo: R$ ", preco_novo)                  # Na tela de interação, o calculo do preço novo ja realizado se apresentara junto com a str.
elif preco_antigo >= 100:
	preco_novo = (preco_antigo * 0.2) + preco_antigo
	print(" Preço novo: R$ ", preco_novo )

if preco_novo > 0.01 and preco_novo < 50:                  # Utilizando os valores do preço novo, ele se adequara nas seguintes condiçoes.
	print(" Selo: Azul")
elif preco_novo > 50.01 and preco_novo < 99.99:
	print(" Selo: Verde")
elif preco_novo > 100 and preco_novo < 199:
	print(" Selo: Amarelo")
elif preco_novo > 200:
	print(" Selo: Vermelho")











