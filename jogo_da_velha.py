
tabuleiro = [[' ', ' ', ' '],  # Linha 1
             [' ', ' ', ' '],  # Linha 2
             [' ', ' ', ' ']]  # Linha 3


def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 9)


# Função para verificar se alguém ganhou
def verificar_vitoria():
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return True

    # Verificar colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return True

    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return True

    return False

# Função principal para o jogo
def jogar():
    jogador_atual = 'X' 
    while True:
        mostrar_tabuleiro()  
        print(f"Vez do jogador {jogador_atual}")

        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Essa posição já está ocupada! Tente outra.")
            continue

        if verificar_vitoria():
            mostrar_tabuleiro()
            print(f"Jogador {jogador_atual} venceu!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar()


