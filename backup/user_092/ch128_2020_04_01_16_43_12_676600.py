p1 = str(input("Está se movendo?(n/s) "))
if p1 == "s":
    p2 = str(input("Deveria se mover?(n/s) "))
    if p2 == "s":
        print("Sem problemas!")
    else:
        print("Silver tape")
else:
    p3 = str(input("Deveria estar parado?(n/s) "))
    if p3 == "s":
        print("Sem problemas!")
    else:
        print("WD-40")