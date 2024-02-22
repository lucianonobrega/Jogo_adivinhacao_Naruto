from random import choice
from time import sleep
import os

lista_naruto = ["naruto","sasuke","sakura","kakashi","iruka",
                "jiraiya","tsunate","orochimaru","itachi",
                "kisame","nagato","konan","deidara","sasori",
                "hidan","kakuzu","obito","zetsu","hiruzen","tobirama",
                "hashirama","minato","kushina","shikamaru","ino","chouji",
                "neji","rocklee","tenten","gaara","kankuro","temari","kiba",
                "hinata","shino","kurama","kurenai","asuma","mightguy","madara"]

def apresentacao():
    print("-" * 30)
    print("| Jogo da Adivinhação Naruto |")
    print("-" * 30)

def cpu_palavra_secreta():
    palavra_secreta = choice(lista_naruto)
    return palavra_secreta

def jogar_novamente():
    while True:
        continuar = str(input("Deseja jogar novamente?[S/N]: ")).upper()
        if continuar == "S":
            break
        elif continuar == "N":
            print("Até a próxima! ;)")
            sleep(2)
            exit()
        else:
            print("Opção inválida.\nPor favor, tente novamente.")
            sleep(2)

def jogo():
    while True:
        os.system("cls")
        apresentacao()
        personagem = cpu_palavra_secreta()
        tentativas = 3
        secreto = ["_"] * len(personagem)
        while True:
            try:
                print("Descubra o nome do personagem!")
                print(secreto)
                palpite = str(input("Letra: ")).lower()
                for l in range(len(personagem)):
                    if palpite == personagem[l]:
                        secreto[l] = palpite
                if palpite not in personagem:
                    tentativas -= 1
                    print(f"Tentativas: {tentativas}.")
                    if tentativas == 0:
                        print(f"Você perdeu!\nO personagem é: {personagem}.")
                        sleep(2)
                        jogar_novamente()
                        break
                if "".join(secreto) == personagem:
                    print(secreto)
                    print("Parabéns! Você acertou!")
                    sleep(2)
                    jogar_novamente()
                    break
                if len(palpite) > 1:
                    print("Digite apenas letras, por favor!")
                    sleep(2)
            except ValueError:
                print(f"Ocorreu um problema: Digite apenas os números correspondentes das opções.")
                sleep(2)

if __name__ == "__main__":
    jogo()