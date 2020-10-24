fato = True
while fato:
    fato = input("Você tem duvidas na disciplina? ")
    if fato != "não":
        print("Pratique mais")
    else:
        print("Até a próxima")
        fato = False
    
