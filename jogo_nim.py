def computador_escolhe_jogada(n, m):
    achouMultiplo = False    
    if n <= m:
        m = n
    else:
        pecas_retirar = n % (m+1)
        if pecas_retirar > 0:
            m = pecas_retirar        
    if m == 1:
        print("O computador tirou uma peça")
    else:
        print("O computador tirou",m,"peças")
    return m

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    pecas_retirar = 0
    while not jogada_valida:
        pecas_retirar = int(input("Quantas peças você vai tirar? "))
        if pecas_retirar < 1 or pecas_retirar > m or pecas_retirar > n:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            jogada_valida = True

    if pecas_retirar == 1:
        print("Você tirou uma peça")
    else:
        print("Você tirou",pecas_retirar,"peças")

    return pecas_retirar

def partida():
    print("")
    pecas = int(input("Quantas peças? "))
    pecas_limite = int(input("Limite de peças por jogada? "))
    
    print("")
    jogador = defineJogadorInicio(pecas, pecas_limite)

    while pecas > 0:
        
        if jogador == 1:
            pecas = pecas - usuario_escolhe_jogada(pecas, pecas_limite)
        else:
            pecas = pecas - computador_escolhe_jogada(pecas, pecas_limite)          
        
        if not defineVencedor(jogador,pecas):
            print("Agora restam",pecas,"peças no tabuleiro.\n")
            jogador = defineJogador(jogador)

def defineVencedor(jogador, n):
    if n == 0:
        if jogador == 1:
            print("Fim do jogo! Você ganhou!\n")
        else:    
            print("Fim do jogo! O computador ganhou!\n")
        return True    
    else:
        return False        

def defineJogadorInicio(n,m):
    if n % (m + 1) == 0:        
        print("Voce começa! \n")
        return 1
    else:
        print("Computador começa! \n")
        return 2

def defineJogador(jogador):
    if jogador == 1:
        return 2
    else:
        return 1
        
def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    
    i = 1
    while i < 4:
        print("**** Rodada",i,"****")
        partida()
        i = i + 1  
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você 0 x 3 Computador")

print("Bem-vindo ao jogo no NIM! Escolha:")
print("")

tipoPartida = int(input("1 - para jogar uma partida isolada \n"
                        "2 - para jogar um campeonato "))
if tipoPartida == 2:
    campeonato()
else:
    partida()