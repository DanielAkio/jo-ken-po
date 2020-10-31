def main():
    jogar_novamente = "1"
    mostra_qual_jogo_esta_sendo_jogado()
    primeiro_jogador = qual_nome_do_primeiro_jogador()
    segundo_jogador = qual_nome_do_segundo_jogador()
    while(jogar_novamente == "1"):
        um_monte_de_espaco()
        jogada_do_primeiro_jogador = validar_jogada(pergunta_jogada_do_primeiro_jogador(primeiro_jogador))
        while(not jogada_do_primeiro_jogador):
            jogada_do_primeiro_jogador = validar_jogada(pergunta_jogada_do_primeiro_jogador(primeiro_jogador))
        um_monte_de_espaco()
        jogada_do_segundo_jogador = validar_jogada(pergunta_jogada_do_segundo_jogador(segundo_jogador))
        while(not jogada_do_segundo_jogador):
            jogada_do_segundo_jogador = validar_jogada(pergunta_jogada_do_segundo_jogador(segundo_jogador))
        um_monte_de_espaco()
        jogada_do_primeiro_jogador_palavra = qual_o_primeiro_jogador_jogou(jogada_do_primeiro_jogador)
        jogada_do_segundo_jogador_palavra = qual_o_segundo_jogador_jogou(jogada_do_segundo_jogador)
        mostra_o_que_cada_um_jogou(primeiro_jogador, segundo_jogador, jogada_do_primeiro_jogador_palavra, jogada_do_segundo_jogador_palavra)
        quem_ganhou(primeiro_jogador, segundo_jogador, jogada_do_primeiro_jogador_palavra, jogada_do_segundo_jogador_palavra)
        jogar_novamente = quer_jogar_novamente()
        if jogar_novamente == "1":
            um_monte_de_espaco()
    mensagem_de_adeus()



def mostra_qual_jogo_esta_sendo_jogado():
    print("\n")
    print("*********************************")
    print("*** Voce vai jogar jo-ken-po! ***")
    print("*********************************")

def qual_nome_do_primeiro_jogador():
    return input("\nQual o nome do primeiro jogador?\n")

def qual_nome_do_segundo_jogador():
    return input("\nQual o nome do segundo jogador?\n")

def um_monte_de_espaco():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def pergunta_jogada_do_primeiro_jogador(primeiro_jogador):
    return input(f"\n{primeiro_jogador} escolha entre: \n\n(1) Pedra \n(2) Papel \n(3) Tesoura\n\n")

def pergunta_jogada_do_segundo_jogador(segundo_jogador):
    return input(f"\n{segundo_jogador} escolha entre: \n\n(1) Pedra \n(2) Papel \n(3) Tesoura\n\n")

def qual_o_primeiro_jogador_jogou(jogada_do_primeiro_jogador):
    if jogada_do_primeiro_jogador == 1:
        jogada = "Pedra"
    if jogada_do_primeiro_jogador == 2:
        jogada = "Papel"
    if jogada_do_primeiro_jogador == 3:
        jogada = "Tesoura"
    return jogada

def qual_o_segundo_jogador_jogou(jogada_do_segundo_jogador):
    if jogada_do_segundo_jogador == 1:
        jogada = "Pedra"
    if jogada_do_segundo_jogador == 2:
        jogada = "Papel"
    if jogada_do_segundo_jogador == 3:
        jogada = "Tesoura"
    return jogada

def mostra_o_que_cada_um_jogou(primeiro_jogador, segundo_jogador, jogada_do_primeiro_jogador, jogada_do_segundo_jogador):
    print(f"O {primeiro_jogador} jogou {jogada_do_primeiro_jogador} e o {segundo_jogador} jogou {jogada_do_segundo_jogador}\n")

def quem_ganhou(primeiro_jogador, segundo_jogador, jogada_do_primeiro_jogador, jogada_do_segundo_jogador):
    if jogada_do_primeiro_jogador == jogada_do_segundo_jogador:
        print("Empate")
    elif (jogada_do_primeiro_jogador == "Pedra" and jogada_do_segundo_jogador == "Tesoura") or \
       (jogada_do_primeiro_jogador == "Papel" and jogada_do_segundo_jogador == "Pedra") or \
       (jogada_do_primeiro_jogador == "Tesoura" and jogada_do_segundo_jogador == "Papel"):
        print(f"O {primeiro_jogador} ganhou!!")
    else:
        print(f"O {segundo_jogador} ganhou!!")

def quer_jogar_novamente():
    return input(f"\nDeseja jogar novamente boiolao? \n\n(1) Sim \n(2) Nao\n")

def validar_jogada(jogada):
    if jogada == "":
        print("\nVoce eh burro? Escreve um valido ai mermao \n")
        return False
    jogada = int(float(jogada))
    if jogada != 1 and jogada != 2 and jogada != 3:
        print("\nVoce eh burro? Escreve um valido ai mermao \n")
        return False
    return jogada

def mensagem_de_adeus():
    print("\nObrigado por jogar, esperamos que vc tenha se divertido!\n")
    print("\nCriadores:")
    print("- Felipe Maeta dos Santos")
    print("- Daniel Akio Teixeira")

if __name__ == "__main__":
    main()
