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

maquina = "on"

print("Máquina ligada.")

operacoes = ["+", "-", "*", "/"]

while maquina == "on":
    operacao = ""
    while operacao not in operacoes and operacao != "off":
        operacao = input("Digite a operação que pretende efetuar (+, -, *, / ou off para desligar): ")

    if operacao in operacoes:
        numero1 = input("Digite o 1º número (off para desligar): ")

        if numero1 == "off":
            maquina = numero1
        else:
            numero2 = input("Digite o 2º número (off para desligar): ")

            if numero2 == "off":
                maquina = numero2
            else:
                numero1 = float(numero1)
                numero2 = float(numero2)

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
                

    else:
        maquina = operacao

print ("Máquina desligada.")
