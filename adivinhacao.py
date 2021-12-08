import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 100)
    tentativas = 30
    pontos = 1000

    print("DIFICULDADE")
    print("Fácil (1), Médio (2), Difícil (3)")

    nivel = int(input("Digite o nível de dificuldade desejado: "))

    if nivel == 1:
        tentativas = tentativas // nivel
    elif nivel == 2:
        tentativas = tentativas // nivel
        pontos = pontos * nivel
    elif nivel == 3:
        tentativas = tentativas // nivel
        pontos = pontos * nivel
    else:
        print("Dificuldade inválida.")

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}:".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if chute < 1 or chute > 100:
            print("Inválido! Você deve digitar um número entre 1 e 100")
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acerto:
            print("Correto!")
            print("Tentativas utilizadas: {}".format(rodada))
            print("Obteve {} pontos".format(pontos))
            break
        elif maior:
            print("Errado... O seu chute foi maior que o número secreto")
            pontos = pontos - (abs(numero_secreto - chute) * nivel)
            if rodada == tentativas:
                print("O número secreto era {}. Você terminou com {}".format(numero_secreto, pontos))
        elif menor:
            print("Errado... O seu chute foi menor que o número secreto")
            pontos = pontos - (abs(numero_secreto - chute) * nivel)
            if rodada == tentativas:
                print("O número secreto era {}. Você terminou com {}".format(numero_secreto, pontos))

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
