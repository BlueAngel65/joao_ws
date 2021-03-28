"""

    Escreva um programa que determina o maior inteiro (n) tal que:

        1+2+...+n <= limite

    Em que o limite é o valor lido pelo programa.

    Exemplo do programa:

        Qual o valor de limite?
        ? 10
        O maior inteiro é 4

"""

limite = int(input("Valor de limite:"))

inteiro = 0
soma = 0
while soma < limite:
    inteiro += 1
    soma += inteiro

if soma > limite:
    inteiro -= 1

print("O maior inteiro é", inteiro)
