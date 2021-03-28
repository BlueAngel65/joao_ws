"""

    Escreva um programa que receba dois valores correspondentes ao primeiro e último nome de uma pessoa e 
    apresente no ecrã esse nome no seguinte formato: apelido, nome.

"""

nome = ""
apelido = ""

while nome == "":
    nome = input("Nome: ")

while apelido == "":
    apelido = input("Apelido: ")

print("Nome:", apelido+", "+nome)