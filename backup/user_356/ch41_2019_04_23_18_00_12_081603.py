tentar=True
while tentar:
    resposta=input("Tente adivinhar a senha: ")
    if resposta==("desisto"):
        tentar=False
        print("Você acertou a senha!")
    else:
        resposta=input("Tente adivinhar a senha: ")