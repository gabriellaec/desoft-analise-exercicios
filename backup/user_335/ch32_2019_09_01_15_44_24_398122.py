pergunta = True

while pergunta:
    resposta = input("Você possui dúvidas na disciplina? ")
    if resposta != "não":
        print ("Pratique mais")
        resposta = input("Você possui dúvidas na disciplina? ")
    else:
        print ("Até a próxima")
        pergunta = False