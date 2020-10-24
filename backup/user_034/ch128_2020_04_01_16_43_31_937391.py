a = input("Está se movendo?: (s ou n)")
if a == "n":
    b = input("Deveria estar parado?: (s ou n)")
    if b == "n":
        print ("WD-40")
    elif b == "s":
        print ("Sem Problemas!")
else:
    c = input("Deveria se mover?: (n ou s)")
    if c == "n":
        print ("Silver tape")
    elif c == "s":
        print ("Sem problemas")