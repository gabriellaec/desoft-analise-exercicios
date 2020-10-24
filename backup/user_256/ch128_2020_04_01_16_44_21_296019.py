movendo = input("O objeto esta se movendo? s ou n ? ")
if movendo == "s":
    deveriamover = input("Deveria se mover? s ou n ? ")
    if deveriamover == "s":
        print("Sem problemas!")
    elif deveriamover == "n":
        print("Silver tape")
if movendo == "n":
    deveriaparado = input("Deveria estar parado? s ou n ? ")
    if deveriaparado == "s":
        print("Sem problemas!")
    elif deveriaparado == "n":
        print("WD-40")