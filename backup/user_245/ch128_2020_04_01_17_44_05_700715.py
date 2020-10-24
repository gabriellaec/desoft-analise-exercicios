mov = input("O objeto está se movendo? s/n ")
if mov == 's':
    movendo = input("Ele deveria se mover? s/n ")
    if movendo == "s":
        print ("Sem problemas!")
    elif movendo == "n":
        print ("Silver tape")
elif mov == 'n':
    parado = input("Ele deveria estar parado? s/n ")
    if parado == "s":
        print ("Sem problemas!")
    elif parado == 'n':
        print ("WD-40")