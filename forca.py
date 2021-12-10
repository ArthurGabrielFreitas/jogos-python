import util
import random





def jogar():
    imprimir_mensagem_inicio()

    nome_arquivo = "cidades.txt"
    palavra_secreta_tuple = carregar_palavra_secreta(nome_arquivo)
    palavra_secreta_display = palavra_secreta_tuple[0]
    palavra_secreta = palavra_secreta_tuple[1]  # Palavra formatada para maiúsculo e sem acentos
    letras_chutadas = []

    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print("\t\t{}".format(letras_acertadas))

    enforcado = False  # Condição de derrota
    acerto = False  # Condição de vitória
    tentativas = 0
    limite_tentativas = 7

    # Laço do jogo
    while not enforcado and not acerto:

        chute = retorna_chute(letras_chutadas, palavra_secreta)

        if chute != "@":
            letras_chutadas.append(chute)
        # Caso de o chute ser igual à palavra
        if chute == "*":
            acerto = True
            break

        # Verifica se a letra chutada existe na palavra.
        posicao = palavra_secreta.find(chute)
        if posicao > -1:
            computar_chute_correto(chute, posicao, palavra_secreta, letras_acertadas)
            print("\t\tCorreto!")
        # A letra chutada não foi encontrada na palavra
        else:
            tentativas += 1
            print("\t\tErrado! Tentativas restantes: {}".format(limite_tentativas - tentativas))

        imprimir_forca(tentativas)
        print("\t\tVocê chutou as letras {}".format(letras_chutadas))
        print("\t\t{}".format(letras_acertadas))

        # Faz as verificações das condições de derrota ou vitória
        enforcado = tentativas == limite_tentativas
        acerto = "-" not in letras_acertadas
    if acerto:
        imprimir_mensagem_vitoria(palavra_secreta_display)
    else:
        imprimir_mensagem_derrota(palavra_secreta_display)
    print("\n\t\tFim do jogo!")


def imprimir_mensagem_inicio():
    print("\t\t********************************************************************************")
    print("\t\tBem vindo ao jogo de Forca!")
    print("\t\tVocê pode chutar uma letra por vez ou chutar a palavra inteira.")
    print("\t\tNão utilize caracteres especiais nem espaços, mesmo se chutar a palavra inteira.")
    print("\t\tBom jogo!!!")
    print("\t\t********************************************************************************")


def imprimir_forca(erros):
    print("\t\t  _______     ")
    print("\t\t |/      |    ")

    if (erros == 1):
        print("\t\t |      (_)   ")
        print("\t\t |            ")
        print("\t\t |            ")
        print("\t\t |            ")

    if (erros == 2):
        print("\t\t |      (_)   ")
        print("\t\t |      \     ")
        print("\t\t |            ")
        print("\t\t |            ")

    if (erros == 3):
        print("\t\t |      (_)   ")
        print("\t\t |      \|    ")
        print("\t\t |            ")
        print("\t\t |            ")

    if (erros == 4):
        print("\t\t |      (_)   ")
        print("\t\t |      \|/   ")
        print("\t\t |            ")
        print("\t\t |            ")

    if (erros == 5):
        print("\t\t |      (_)   ")
        print("\t\t |      \|/   ")
        print("\t\t |       |    ")
        print("\t\t |            ")

    if (erros == 6):
        print("\t\t |      (_)   ")
        print("\t\t |      \|/   ")
        print("\t\t |       |    ")
        print("\t\t |      /     ")

    if (erros == 7):
        print("\t\t |      (_)   ")
        print("\t\t |      \|/   ")
        print("\t\t |       |    ")
        print("\t\t |      / \   ")

    print("\t\t |            ")
    print("\t\t_|___         ")
    print()


def imprimir_mensagem_vitoria(palavra_secreta_display):
    print("\t\tVocê acertou a palavra {}!".format(palavra_secreta_display))
    print("\t\t       ___________      ")
    print("\t\t      '._==_==_=_.'     ")
    print("\t\t      .-\\:      /-.    ")
    print("\t\t     | (|:.     |) |    ")
    print("\t\t      '-|:.     |-'     ")
    print("\t\t        \\::.    /      ")
    print("\t\t         '::. .'        ")
    print("\t\t           ) (          ")
    print("\t\t         _.' '._        ")
    print("\t\t        '-------'       ")


def imprimir_mensagem_derrota(palavra_secreta_display):
    print("\t\tVocê perdeu TUDO.")
    print("\t\t    _______________         ")
    print("\t\t   /               \       ")
    print("\t\t  /                 \      ")
    print("\t\t//                   \/\  ")
    print("\t\t\|   XXXX     XXXX   | /   ")
    print("\t\t |   XXXX     XXXX   |/     ")
    print("\t\t |   XXX       XXX   |      ")
    print("\t\t |                   |      ")
    print("\t\t \__      XXX      __/     ")
    print("\t\t   |\     XXX     /|       ")
    print("\t\t   | |           | |        ")
    print("\t\t   | I I I I I I I |        ")
    print("\t\t   |  I I I I I I  |        ")
    print("\t\t   \_             _/       ")
    print("\t\t     \_         _/         ")
    print("\t\t       \_______/           ")
    print("\t\tA palavra era {}".format(palavra_secreta_display))


def carregar_palavra_secreta(nome_arquivo):
    arquivo = open("cidades.txt", "r", -1, "utf-8")

    cidades = []
    for linha in arquivo:
        linha = linha.strip("\n")
        cidades.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(cidades))
    palavra = cidades[numero]
    palavra_secreta_tuple = (palavra.strip(), util.ignora_acento(palavra.upper().replace(" ", "")))
    return palavra_secreta_tuple


# Cria uma lista para mostrar na tela os espaços das letras da palavra secreta e as letras que forem acertadas
def inicializar_letras_acertadas(palavra):
    return ["-" for letra in palavra]





def retorna_chute(letras_chutadas, palavra_secreta):
    chute = util.ignora_acento(input("\t\tChute uma letra sem acento: ").strip().upper())
    if comparar_chute_palavra(chute, palavra_secreta):
        return "*"
    return tratar_chute(chute, letras_chutadas, palavra_secreta)


def comparar_chute_palavra(chute, palavra_secreta):
    return chute == palavra_secreta

def tratar_chute(chute, letras_chutadas, palavra_secreta):
    tamanho = len(chute)
    if tamanho > 1:
        print("\t\tVocê chutou mais de uma letra ou a palavra completa...")
        return "@"
    while not chute.isalpha():
        print("\t\tChute uma letra válida!")
        chute = retorna_chute(letras_chutadas, palavra_secreta)
    while chute in letras_chutadas:
        print("\t\tVocê já fez esse chute!")
        chute = retorna_chute(letras_chutadas, palavra_secreta)
    return chute


# Se o chute estiver contido na palavra, continua procurando a letra chutada na palavra
# A partir do índice + 1 retornado pelo método find() para encontrar todas as instâncias do chute na palavra
def computar_chute_correto(chute, posicao, palavra_secreta, letras_acertadas):
    while posicao > -1:
        letras_acertadas[posicao] = palavra_secreta[posicao]
        posicao = palavra_secreta.find(chute, posicao + 1)





if __name__ == "__main__":
    jogar()
