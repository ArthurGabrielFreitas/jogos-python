import adivinhacao
import forca


def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("Jogos:\nAdivinhação (1), Forca (2), Sair (3)\n")

    jogo = int(input("Qual jogo? "))

    while jogo != 3:
        if jogo == 1:
            print("Jogo de Adivinhação iniciado.\n")
            adivinhacao.jogar()
            jogo = int(input("Escolha um novo jogo:\nAdivinhação (1), Forca (2), Sair (3)\n"))
        elif jogo == 2:
            print("Jogo de Forca iniciado.\n")
            forca.jogar()
            jogo = int(input("Escolha um novo jogo:\nAdivinhação (1), Forca (2), Sair (3)\n"))
        else:
            print("Valor de jogo inválido.")
            jogo = int(input("Escolha um novo jogo:\nAdivinhação (1), Forca (2), Sair (3)\n"))

    print("*********************************")
    print("*******Obrigado por jogar!*******")
    print("*********************************")


if __name__ == "__main__":
    escolher_jogo()
