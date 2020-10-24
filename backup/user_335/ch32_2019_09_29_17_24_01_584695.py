resposta = input("Você possui dúvidas na disciplina? ")

while resposta:
    if resposta != "não":
        print ("Pratique mais")
        resposta = input("Você possui dúvidas na disciplina? ")
    else:
        print ("Até a próxima")
        resposta = False