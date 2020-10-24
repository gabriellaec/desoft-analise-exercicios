pergunta = True
while pergunta:
    questao = input("Você tem dúvidas?")
    if questao != "não":
        print("Pratique mais")
    else:
        print("Até a próxima")
        pergunta = False