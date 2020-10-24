executa=input("Código está executando?")
avancar=0
while not avancar:
    if executa=="n":
        print("Corrija o código e tente de novo")
        executa=input("Código está executando?")
    if executa=="s":
        resultado=input("O código produz o resultado correto?")
        if resultado=="n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        elif resultado=="s":
            print("Parabéns!")
            break
        avancar=True
        