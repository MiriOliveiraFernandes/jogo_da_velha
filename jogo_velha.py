tabuleiro = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"]
]

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


jogadas = 0
vez_jogador = "X"

#Definir uma função -> estrutura necassária para a criação de uma função
def apresentaTabuleiro():
    #array sempre se lê [linha][coluna]
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])

def checkVencedor():
    for linha in range(3):
        concatLinha = tabuleiro[linha][0] + tabuleiro[linha][1]+ tabuleiro[linha][2]
        if concatLinha =="XXX" or concatLinha =="OOO":
            print("vC TEM U M VENCEDER")
    
    for coluna in range(3):
        concatColuna = tabuleiro[0][coluna] + tabuleiro[1][coluna]+ tabuleiro[2][coluna]
        if concatColuna =="XXX" or concatColuna =="OOO":
            print("vC TEM U M VENCEDER")
    
    #vertical
    if tabuleiro[0][0] == tabuleiro[1][1]== tabuleiro[2][2] or \
     tabuleiro[0][2] == tabuleiro[1][1]== tabuleiro[2][0]:
        print("vC TdaEM U M VENCEDER")

    
apresentaTabuleiro()

while jogadas < 9:
    posicao = input("Inserir a posição desejada: ")
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == posicao: #estou acessando um array
                tabuleiro[linha][coluna] = vez_jogador #modificando uma posição do array
                jogadas = jogadas + 1
                if vez_jogador =="X":
                    vez_jogador="O"
                else:
                    vez_jogador = "X"
                break
    checkVencedor()
    apresentaTabuleiro()


# print(tabuleiro)