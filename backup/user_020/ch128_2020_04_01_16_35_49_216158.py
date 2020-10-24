pergunta1 = input("Está se movendo? n/s")
if pergunta1 == 'n':
    parado = input("Deveria estar parado? n/s")
    if parado == 'n':
        print("WD-40")
    elif parado == 's':
        print("Sem problemas!")
elif pergunta1 == 's':
    mover = input("Deveria se mover? n/s")
    if mover == 'n':
        print("Silver tape")
    elif mover == 's':
        print("Sem problemas!")