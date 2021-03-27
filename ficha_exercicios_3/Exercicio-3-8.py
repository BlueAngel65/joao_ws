"""

    Escreva um programa que pede ao utilizador nomes até o utilizador escrever “sair”.

    Exemplo do programa:

        Escreva um nome (“sair” para terminar)
        ? Maria
        Escreva um nome (“sair” para terminar)
        ? João
        Escreva um nome (“sair” para terminar)
        ? sair

"""

nome = ""
while nome.lower() != "sair":       ## O método lower() coloca o conteúdo da nome (uma string) todo em minúsculas.
                                    ## Assim, mesmo que escrevam Sair ou SAIR o programa pára.
    nome = input('Escreva um nome ("sair" para terminar): ')
    if nome.lower() != "sair":
        print(nome)
    else:
        print("Fim do ciclo.")

