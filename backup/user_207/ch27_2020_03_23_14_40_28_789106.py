duvida_na_disciplina = True

while duvida_na_disciplina:
    P = str(input("Você tem dúvidas na disciplina? "))
    if P != "não":
        print ("Pratique mais")
    else:
        print ("Até a próxima")
        duvida_na_disciplina = False
