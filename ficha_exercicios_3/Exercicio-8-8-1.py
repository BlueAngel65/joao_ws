"""

    Escreva um programa que simule uma calculadora básica e que por isso permita as quatro operações básicas: 
        somar, 
        subtrair, 
        multiplicar e 
        dividir. 
    
    O utilizador deve escolher a operação que pretende. 
    De seguida o programa deve pedir DOIS números e aplicar a operação anteriormente escolhida. 
    Por fim, deve imprimir o resultado da operação matemática efetuada.

"""

operacoes = ["+", "-", "*", "/"]

operacao = ""
while operacao not in operacoes:
    operacao = input("Digite a operação que pretende efetuar: ")

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

resultado = 0
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif numero2 == 0:                      ## Se chegamos atá aqui é porque é uma divisão
    resultado = "ERR"
else:
    resultado = numero1 / numero2

print(numero1, operacao, numero2, " = ", resultado)
