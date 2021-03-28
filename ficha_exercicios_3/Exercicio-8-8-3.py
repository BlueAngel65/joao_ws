"""

    Escreva um programa que simule uma calculadora básica e que por isso permita as quatro operações básicas: 
        somar, 
        subtrair, 
        multiplicar e 
        dividir. 
    
    O utilizador deve escolher a operação que pretende. 
    De seguida o programa deve pedir dois números e aplicar a operação anteriormente escolhida. 
    Por fim, deve imprimir o resultado da operação matemática efetuada.

"""

def operacao_ecra(lista):
    operacao = ""
    for item in lista:
        operacao += " "+str(item)

    return operacao

"""
    print(multiplicacao)
    print(divisao)

"""

def opera(lista, operacoes):

    lista_resultado = lista[:-1].copy() if lista[-1] in operacoes else lista.copy()

    ## Multiplicação e divisão em primeiro lugar.
    while "*" in lista_resultado or "/" in lista_resultado:
        multiplicacao = lista_resultado.index("*") if "*" in lista_resultado else 0
        divisao = lista_resultado.index("/") if "/" in lista_resultado else 0

        if multiplicacao != 0 or divisao != 0:
            if multiplicacao != 0 and multiplicacao < divisao or divisao == 0:
                lista_resultado[multiplicacao-1] = lista_resultado[multiplicacao-1]*lista_resultado[multiplicacao+1]
                elimina = multiplicacao
            else:
                lista_resultado[divisao-1] = lista_resultado[divisao-1]/lista_resultado[divisao+1]
                elimina = divisao

            del lista_resultado[elimina: elimina+2]

    ## As restantes operações em último
    operacao = ""
    resultado = 0
    for item in lista_resultado:
        if item in operacoes:
            operacao = item
        elif operacao == "":
            resultado = item
        elif operacao == "-":
            resultado -= item
        else:
            resultado += item

    ##print(lista)
    ##print(lista_resultado)

    return resultado

operacoes = ["+", "-", "*", "/", "!", "=", "#", "C", "c"]

lista = []
display = ""
operacao = ""
resultado = 0
entrada = ""

while entrada != "#":
    entrada = input("(# para terminar): ")

    if entrada != "#":
        if entrada in ["C", "c", "="]:
            operacao = entrada
            if entrada in ["C", "c"]:
                lista = []
                resultado = 0
                
        elif entrada in operacoes:
            operacao = entrada
            if len(lista) > 0:
                if lista[-1] in operacoes:
                    lista[-1] = operacao
                else:
                    lista += operacao

        else:
            try:
                valor = float(entrada)
                if len(lista) == 0 or lista[-1] in operacoes:
                    lista += [valor]
                else:
                    lista[-1] = valor
                resultado = opera(lista, operacoes)
            except ValueError:
                print("Entrada inválida.")

        display = operacao_ecra(lista)
        if (operacao == "="):
            print(display+" = "+str(resultado))
            lista = []
            resultado = 0
            operacao = ""
        else:
            print(display+" (= "+str(resultado)+")")

    ##print(lista)
