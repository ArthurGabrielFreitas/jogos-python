import util
import random


def jogar():
    imprimir_mensagem_inicio()

    palavra_secreta_tuple = carregar_palavra_secreta()
    palavra_secreta_display = palavra_secreta_tuple[0]
    palavra_secreta = palavra_secreta_tuple[1]  # Palavra formatada para maiúsculo e sem acentos

    # Cria uma lista para mostrar na tela os espaços das letras da palavra secreta e as letras que forem acertadas
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcado = False  # Condição de derrota
    acerto = False  # Condição de vitória
    tentativas = 0
    limite_tentativas = 6

    # Laço do jogo
    while not enforcado and not acerto:

        chute = input("Chute uma letra sem acento: ").strip().upper()

        # Verifica se a letra chutada existe na palavra.
        # Se sim, continua procurando a letra chutada na palavra a partir do índice + 1 retornado pela função find()
        posicao = palavra_secreta.find(chute)
        if posicao > -1:
            while posicao > -1:
                letras_acertadas[posicao] = palavra_secreta_display[posicao]
                posicao = palavra_secreta.find(chute, posicao + 1)
        # A letra chutada não foi encontrada na palavra
        else:
            tentativas += 1
            print("Errado! Tentativas restantes:", limite_tentativas - tentativas)

        print(letras_acertadas)

        # Faz as verificações das condições de derrota ou vitória
        enforcado = tentativas == limite_tentativas
        acerto = "-" not in letras_acertadas

        # Código da aula para verificar se a letra chutada existe na palavra
        # index = 0
        # for letra in palavra_secreta:
        #     if chute == letra:
        #         print("Letra {} na posição {}".format(letra, index))
        #     index = index + 1

    if acerto:
        print("Você acertou a palavra {}!".format(palavra_secreta_display))
    else:
        print("Você perdeu TUDO.")

    print("\nFim do jogo!")


def imprimir_mensagem_inicio():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")

    cidades = []
    for linha in arquivo:
        linha = linha.strip()
        cidades.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(cidades))
    palavra = cidades[numero][:-4].strip()
    palavra_secreta_tuple = (palavra.capitalize(), util.ignora_acento(palavra.upper()))
    return palavra_secreta_tuple


def inicializar_letras_acertadas(palavra):
    return ["-" for letra in palavra]


if __name__ == "__main__":
    jogar()
