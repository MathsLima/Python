"""
Associe a uma variável no seu programa uma string entre “”” que contenha seu parágrafo favorito - talvez um poema, uma fala, instruções para assar um bolo, etc.

Escreva uma função que conta o número de letras (a até z, ou A até Z) em seu texto e então conta quantas são a letra ‘e’. Sua função deve exibir uma análise o texto desta forma::
"""
def count(p):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0   #numeros de e's
    totalChars = 0  #numeros de caracteres
    for achar in p:
        if achar in lows or achar in ups:  #se achar for minusculo ou maiscula ele vai para a linha 14.
            totalChars = totalChars + 1    #conta o total de caracteres
            if achar == 'e':       # se a letra contada for e, vai somando a ca lasso
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    print("Seu texto contém", totalChars, "caracteres, dos quais", numberOfe, "(", percent_with_e, "%)", "são 'e'.")


p = '''
"If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely
'''

count(p)
