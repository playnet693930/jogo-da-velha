def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 9)


def verificar_vitoria(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False


def jogar():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador = "X"

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Parabéns! O jogador", jogador, "venceu!")
            break

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

        # Verificar se deu empate
        if all(tabuleiro[linha][coluna] != " " for linha in tabuleiro for coluna in linha):
            exibir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedor.")
            break


jogar()
