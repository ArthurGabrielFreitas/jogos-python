def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    palavra_secreta = "adivinhacao".upper()
    letras_acertadas = ["-" for letra in palavra_secreta]

    print(letras_acertadas)

    enforcado = False
    acerto = False
    tentativas = 0
    limite_tentativas = 6

    while not enforcado and not acerto:

        chute = input("Chute uma letra: ").strip().upper()

        posicao = palavra_secreta.find(chute)
        if posicao > -1:
            while posicao > -1:
                letras_acertadas[posicao] = chute
                posicao = palavra_secreta.find(chute, posicao + 1)
        else:
            tentativas += 1
            print("Errado! Tentativas restantes:", limite_tentativas - tentativas)

        print(letras_acertadas)

        enforcado = tentativas == limite_tentativas
        acerto = "-" not in letras_acertadas

        # index = 0
        # for letra in palavra_secreta:
        #     if chute == letra:
        #         print("Letra {} na posição {}".format(letra, index))
        #     index = index + 1

    if acerto:
        print("Você acertou a palavra!")
    else:
        print("Você perdeu TUDO.")

    print("\nFim do jogo!")


if __name__ == "__main__":
    jogar()
