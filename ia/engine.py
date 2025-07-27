import random
#from ia.utils import gerar_numero_secreto




def iniciar_jogo(): 
    numero_secreto = random.randint(1, 100)  #gerar_numero_secreto(1, 100)
    palpite_minimo = 1
    palpite_maximo = 100
    tentativas = 0

    print("Adivinhação inicializada!")

    while True:
        try:
            palpite = int(input(f"Digite um palpite entre {palpite_minimo} e {palpite_maximo}: "))
            tentativas += 1

            if palpite < palpite_minimo or palpite > palpite_maximo:
                print(f"Palpite inválido! Deve ser entre {palpite_minimo} e {palpite_maximo}.")
                continue

            if palpite < numero_secreto:
                print("Muito baixo!")
                palpite_minimo = max(palpite_minimo, palpite + 1)
            elif palpite > numero_secreto:
                print("Muito alto!")
                palpite_maximo = min(palpite_maximo, palpite - 1)
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

