"""

    Escreva um programa que lê uma sequência de dígitos, um dígito por linha, até o utilizador inserir -1. No final mostra o número inteiro composto pelos dígitos inseridos pelo utilizador.

    Exemplo do programa:

        Escreva um dígito (-1 para terminar)
        ? 5
        Escreva um dígito (-1 para terminar)
        ? 3
        Escreva um dígito (-1 para terminar)
        ? 9
        Escreva um dígito (-1 para terminar)
        ? -1
        O número é: 539

"""

numero = 0
digito = 0

while digito != -1:

    digito = int(input("Escreva um dígito (-1 para terminar): "))
    print(digito)

    if (digito >= 0 and digito <= 9):
        numero = numero*10 + digito
    elif digito != -1:
        print("Não e um dígito entre 0 e 9")

print("O número é", numero)
