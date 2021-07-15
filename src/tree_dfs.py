import numpy as np

# 0 empty, 1 X, 2 O

# Classe - Nó (Tabuleiro)
class NodeBoard:

    # Construtor 
    def __init__(self):
        self.state_board = None     # Estado do tabuleiro - Mapeamento de posições
        self.playerX_win = False    # Indica o X como vencedor
        self.playerO_win = False    # Indica o O como vencedor
        self.empate = False         # Indica um nó empate
        self.children = []          # Nós filhos - Tabuleiros filhos 
        
    # Setter - Posições jogadas no tabuleiro (Atualiza tabuleiro)
    def setPositionsPlayed(self, positions_player):
        list_positions = np.zeros(shape=(3, 3))  # [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        
        # Atualiza cada linha da matriz
        for i in range(3):
            list_positions[i] = positions_player[i]

        self.state_board = list_positions

    # Getter - Posições vazias
    def getEmptyPositions(self):
        positions = []  # Armazena posicoes vazias
        
        for i in range(3):
            for j in range(3):
                # Verifica se a casa do tabuleiro está em branco
                if (self.state_board[i][j] == 0):
                    positions.append([i, j]) # [[1,1], [2,0], [2,1]]
        return positions

    # Status do nó 
    # Retorna 
        # 1 - X vencendor , 2 - O vencedor
        # False - Jogo inacabado
        # "EMPATE"
    def node_check(self):
        board = self.state_board # Ex: [[2, 2, 1], [1, 0, 2], [0, 0, 1]]

        # linhas
        for i in range(3):
            if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0):
                return board[i][0]

        # coluna
        for i in range(3):
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0):
                return board[0][i]

        # diagonal principal
        if (board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[0][0]

        # diagonal secundaria
        if (board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[0][2]

        # Verifica se tem alguma casa vazia - jogo inacabado
        for i in range(3):
            for j in range(3):
                if (board[i][j] == 0):
                    return False

        return "EMPATE"

# ======================================================================
# ARVORE DE BUSCA

# Jogador X (jogador = 0) : (jogador+1) % 2
# Jogador O (jogador = 1) : (jogador+1) % 2

#        X ,O
token = [1, 2]

def tree(node_board, jogador):
    # Posições do nó tabuleiro 
    board = node_board.state_board
    
    # print(F"\nBoard Inside Tree: \n {board}")
   
    ganhador = node_board.node_check()
    # print(f"\n É ganhador: {ganhador}")

    # Teste se é um nó ganhador para retornar da recursão
    if (ganhador):
        # Ganhador = 1 -> X / Ganhador = 2 -> O / Empate = EMPATE
        if (ganhador == 1):
            node_board.playerX_win = True

        if (ganhador == 2):
            node_board.playerO_win = True

        if (ganhador == 'EMPATE'):
            node_board.empate = True

        return ganhador

    # X -> Jogador 0 / O -> Jogador 1
    jogador_aux = jogador 
    jogador = (jogador + 1) % 2 # Próximo jogador 
    
    # Posicões das casas vazias
    possibilidades = node_board.getEmptyPositions()
    # print(f"\n\n Dentro de Tree - Possibilidade: {possibilidades}")
    
    for possibilidade in possibilidades:
        # possibilidade -> [1,1]

        # Demarca na posição vazia o simbolo do jogador
        board_aux = board.copy() # [[2, 2, 1], [1, 0, 2], [0, 0, 1]]
        board_aux[possibilidade[0], possibilidade[1]] = token[jogador_aux] # token[0] = 1

        # print(f"Possibilidade: {possibilidade[0]}, {possibilidade[1]}")
        # print("\nSub - Board: \n", board_aux, '\n\n')
        
        # Variavel para criar nova classe NodeBoard
        new_board = NodeBoard()
        new_board.setPositionsPlayed(board_aux)

        # Insere no tabuleiro atual como nó filho
        node_board.children.append(new_board)
        
        # print("Children:")
        # for child in node_board.children:
        #     print(child.state_board)
        
        # Recursão
        tree(new_board, jogador)

        # Após a volta de recursão, retira a posição preenchida
        board[possibilidade[0], possibilidade[1]] = 0
        
# ======================================================================

# Mapeando um estado ao conjunto de proximos estados de acordo com as ações possiveis
# Probabilidade (ganhar/perder/empatar) conforme a indicação da próxima jogada
def probability_next_moves(tabuleiro, player):
    for child in tabuleiro.children:
        print("*********************")
        print(f"Tabuleiro:\n {child.state_board}\n")
        print(busca_dfs(child, player))
        print("*********************\n\n")

# DEPTH-FIRST SEARCH (BUSCA EM PROFUNDIDADE)
def busca_dfs(tabuleiro, player):
    playerX_win = 0
    playerO_win = 0
    empate = 0

    v = [tabuleiro]  # Tabuleiro
    levels = [0]

    # print(f"v:{v[0].state_board}")
    # print(f"levels = {levels}")

    while v:

        # Retira o primeiro elemento
        node = v.pop(0)

        # print(f"Tabuleiro Node:\n {node.state_board}")
        
        if node.empate:
            empate += 1
        if node.playerX_win:
            playerX_win += 1
        if node.playerO_win:
            playerO_win += 1

        # level = levels.pop()
        # print(f'Nivel do nó: {level}')

        v = node.children + v

        # print(f"\n v = {v}\n")

        # levels += [level+1]*len(node.children) # levels: [1, 1, 1]
        # print(f"levels: {levels}")
        # print("\n\n")

    total = empate + playerX_win + playerO_win

    ## ====================================
    ## Posteriormente a busca, retorna as porcetagens de vencer, perder ou empatar

    # Player 0 = X 
    # Player 1 = O
    if player == 0:
        player_win_percentage = round(((playerX_win) / total) * 100, 2)
    else:
        player_win_percentage = round(((playerO_win) / total) * 100, 2)

    chance_empatar = round(((empate) / total) * 100, 2)
    chance_perder = round((100 - player_win_percentage - chance_empatar), 2)

    print("Caso seja feito essa jogada: \n")
    return {"Chance_Ganhar": player_win_percentage,
            "Chance_Perder": chance_perder,
            "Chance_Empatar": chance_empatar}

# ======================================================
## TESTES
# ======================================================

# Define tabuleiro
tabuleiro = NodeBoard()

# Setando posições

tabuleiro.setPositionsPlayed([[1, 0, 2],[0, 0, 1],[2, 1, 2]])
#tabuleiro.setPositionsPlayed([[2, 0, 2],[1, 0, 2],[1, 0, 1]]) # OK
# tabuleiro.setPositionsPlayed([[2, 2, 1], [1, 0, 2], [0, 0, 1]]) # OK
#tabuleiro.setPositionsPlayed([[1, 0, 0],[0, 0, 0],[0, 0, 0]])
# tabuleiro.setPositionsPlayed([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# tabuleiro.setPositionsPlayed([[1, 2, 0], [0, 0, 0], [0, 0, 0]])

# Tabuleiro Inicial
# t = tabuleiro.state_board
# print(t,"\n")

# Cria a arvore
    # Tabuleiro - nó raiz
    # Jogador que irá jogar 
        # Jogador X (jogador = 0) | Jogador O (jogador = 1) 
tree(tabuleiro, 0) 

# Probabilidades
probability_next_moves(tabuleiro, 0)


# print(tabuleiro.state_board)
for child in tabuleiro.children:
    print("++++++++++++++++++++++")
    print(child.state_board)
    for i in child.children:
        print("==========================")
        print(i.state_board)

        for j in i.children:
            print("**********************")
            print(j.state_board)