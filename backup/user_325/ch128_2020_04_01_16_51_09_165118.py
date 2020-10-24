funciona = input("Está se movendo?: ")
if funciona == "s":
    mexe = input("Deveria se mover?: ")
    if mexe == "s":
        print("Sem problemas!")
    elif mexe == "n":
        print("Silver tape")
    else:
        print("Digite uma resposta válida!")
if funciona == "n":
    parado=input("Deveria estar parado?: ")
    if parado == "s":
        print("Sem problemas!")
    elif parado == "nao":
        print("WD-40")
    else:
        print("texto inválido, tente novamente!")
        