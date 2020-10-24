palpite = input()
acertou = False
while not acertou:
    palpite = input()
    if palpite == "desisto":
        acertou = True
        print("Você acertou a senha!")
    else:
        palpite = input()