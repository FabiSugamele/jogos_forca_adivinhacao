import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("***Escolha o jogo que deseja!***")
    print("********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Qual jogo deseja? "))

    if(jogo == 1):
        print("Você escolheu Forca")
        forca.jogar()

    elif(jogo == 2):
        print("Você escolheu Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
