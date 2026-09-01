import random

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (1 a 20): "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Acertou! O número era {numero_secreto}. Tentativas: {tentativas}")
        break
    elif palpite < numero_secreto:
        print("O número sorteado é MAIOR.")
    else:
        print("O número sorteado é MENOR.")