"""

    Escreve um programa que lê três números e diz qual é o maior.

    Exemplo do programa:

        Escreva três números separados por vírgula
        ? 6, 19, -3
        O maior: 19

"""

lista = []
for x in range(3):
    numero = int(input("Digite um número: "))
    lista += [numero]

print(lista)
print("O maior número é o", max(lista))
