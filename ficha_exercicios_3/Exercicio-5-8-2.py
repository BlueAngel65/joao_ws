"""

Escreva um programa que lê um número inteiro e calcula a soma dos seus dígitos pares.

    Exemplo do programa:
        Escreva um número inteiro positivo
        ? 234567
        Soma dos dígitos pares: 12

"""

numero = input("Escreva um número inteiro positivo: ")

print(numero)

soma = 0
while numero != "":
    digito = numero[0:1]
    numero = numero[1:]
    if int(digito)/2 == int(int(digito)/2):
        soma += int(digito)

print("A soma dos dígitos pares é ", soma)
