import math
import copy

# Fução para criar tabuleiro vazio
def criaTabuleiro():
  return [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

# Função para Exibir o tabuleiro
def imprimeTabuleiro(tabuleiro):
  print('  1 2 3')
  for i in range(3):
    print('%d' % (i+1), *tabuleiro[i],'', sep = '|')


def actions(s, player) -> "list[tuple]":
    """
    s = game state;
    player = bool (False if Mini, True if Max)

    returns moves
    """
    moves = []
    mark = "x" if player else "o"

    for i in range(3):
        for j in range(3):
            if s[i][j] == " ":
                moves.append((i, j, mark))
    return moves


def result(s, a) -> list[list]:
    s_mod = copia = [list(s[0]),list(s[1]), list(s[2])]
    s_mod[a[0]][a[1]] = a[2]
    return s_mod

def value(p) -> int:
    return 1 if p == "x" else -1


def terminal(s) -> "tuple[bool, int | None]":
    filled = 0
    # verifica se um dos jogadores ganhou o jogo
    for p in ["x", "o"]:
        # verifica se completou uma linha
        for lin in s:
            if (n := lin.count(p)) == 3:
                return (True, value(p))
            filled += n
        # verifica se completou uma coluna
        for i in range(3):
            if s[0][i] == p and s[1][i] == p and s[2][i] == p:
                return (True, value(p))
        # verifica se completou uma diagonal
        if s[1][1] == p and (
            (s[0][0] == p and s[2][2] == p) or (s[0][2] == p and s[2][0] == p)
        ):
            return (True, value(p))

    # verifica se o tabuleiro já foi inteiramente preenchido
    if filled == 9:
        return (True, 0)

    return (False, None)


def minimax(tab, is_max):
    t = terminal(tab)
    if t[0]:
        return (t[1], tab)
    elif is_max:
        s = tab
        v = -math.inf
        for a in actions(tab, is_max):
            r = minimax(result(tab, a), False)
            if r[0] >= v:
              v = r[0]
              s = result(tab, a)
        return (v, s)
    else:
        s = tab
        v = math.inf
        for a in actions(tab, is_max):
            r = minimax(result(tab, a), True)
            if r[0] <= v:
              v = r[0]
              s = result(tab, a)
        return (v, s)
    

# Função Principal
def principal():
  cpuPrimeiro = True
  while(True):
    print('1-CPU 1 x CPU 2\n2-Jogador x CPU\n3-Jogador 1 x Jogador 2')
    op = int(input('4-Sair\nOpção: '))
    vezCPU = True
    if(op>=1 and op<=3):
      while(True):
        tabuleiro = criaTabuleiro()
        output.clear()
        imprimeTabuleiro(tabuleiro)
        vezPrimeiro = True
        while(not terminal(tabuleiro)[0]):
          if(vezCPU and (op == 1 or op == 2)):
            if(vezPrimeiro and cpuPrimeiro):
              aux = minimax(tabuleiro, True)
              tabuleiro = aux[1]
            elif(not vezPrimeiro):
              aux = minimax(tabuleiro, False)
              tabuleiro = aux[1]
          if(op == 2 and not vezCPU or op == 3):
            while(True):
              if(vezPrimeiro and (op == 3 or not cpuPrimeiro)):
                print('Jogador [x]: ')
                valor = 'x'
              else:
                print('Jogador [o]: ')
                valor = 'o'
              linha = int(input('linha: '))
              coluna = int(input('coluna: '))
              if(linha>0 and linha <4 and coluna>0 and coluna <4):
                if(tabuleiro[linha-1][coluna-1]==' '):
                  tabuleiro[linha-1][coluna-1] = valor
                  break
          if(op == 2):
            vezCPU = not vezCPU
          output.clear()
          imprimeTabuleiro(tabuleiro)      
          vezPrimeiro = not vezPrimeiro
        if(op == 2):
          cpuPrimeiro = not cpuPrimeiro
        else:
          cpuPrimeiro = True
        vezCPU = cpuPrimeiro

        resultado = terminal(tabuleiro)
        if(resultado[1] == -1):
          print('Vitória do [o]!')
        elif(resultado[1] == 1):
          print('Vitória do [x]!')
        else:
          print('Empate!')
        while(True):
          saida = input('Jogar novamente?[sim ou não]')
          saida = saida.lower()
          if(saida == 'sim' or saida == 'não'):
            break
        if(saida=='não'):
          break
      output.clear()
    else:
      return

# Execução do programa
principal()

