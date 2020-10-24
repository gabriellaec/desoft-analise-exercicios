i = True

while (i):
    tentativa = input("Qual eh a senha? ")
    if (tentativa != "desisto"):
        print("Tente denovo")
    else:
        i = False
        print("Você acertou a senha!")