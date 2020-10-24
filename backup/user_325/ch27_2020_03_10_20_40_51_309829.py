pergunta = input("Tem duvidas na matéria?: ")
tem_duvida = True
while tem_duvida:
    if pergunta != "não":
        print("Pratique mais")
        pergunta = input("Tem duvidas na matéria?: ")
    else:
        print("Até a próxima")
    break
    