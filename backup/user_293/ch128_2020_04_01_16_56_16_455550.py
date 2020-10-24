pergunta = input("Está se movendo?(n/s) ")

if pergunta == "s":
    p1 = input("Deveria se mover?(n/s) ")
    if p1 == "s":
        print("Sem problemas!")
    elif p1 == "n":
        print("Silver tape")
elif pergunta == "n":
    p2 = input("Deveria estar parado?(n/s) ")
    if p2 == "s":
        print("Sem problemas!")
    elif p2 == "n":
        print("WD-40")