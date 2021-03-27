"""

    Escreva um programa que pede ao utilizador um inteiro correspondente a um número em segundos e calcule o número de horas correspondentes.

    Exemplo do programa:

        Escreva um número em segundos
        ? 3600
        O número de horas correspondente é 1

"""

segundos = int(input("Escreva um número em segundos: "))

horas = segundos/3600

print(segundos, "segundos são", horas)

