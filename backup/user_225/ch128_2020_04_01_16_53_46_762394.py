q1 = input("Está se movendo? ")
if q1 == "s":
    q2 = input("Deveria se mover? ")
    if q2 == "s":
        print("Sem problemas!")
    elif q2 == "n":
        print("Silver tape")
elif q1 == "n":
    q3 = input("Deveria estar parado? ")
    if q3 == "s":
        print("Sem problemas!")
    elif q3 == "n":
        print("WD-40")