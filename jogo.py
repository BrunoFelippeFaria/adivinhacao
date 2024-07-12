from random import randint

tentativas = 0
rand_num = randint(1,100)

print("adivinhe um numero entre 1 e 100")

while True:
    try:
        num = int(input("numero: "))
    except:
        print("porfavor, escolha um numero")
        continue

    tentativas += 1
    if(num == rand_num):
        print(f"parabéns, depois de {tentativas} tentativas você acertou! o numero era {rand_num}")
        break
    elif rand_num > num:
        print(f"você errou, o numero é maior do que {num}")
    elif rand_num < num:
        print(f"você errou, o numero é menor do que {num}")