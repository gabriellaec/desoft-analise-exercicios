sim = ["sim", "s"]
nao = ["nao", "n", "não"]

movendo = input("Esta se movendo?")
if movendo in nao:
    parado = input("Deveria estar parado?")
    if parado in sim:
        print("Sem problemas!")
    elif parado in nao
        print("WD-40")
    else:
        print("Resposta nao existe")
if movendo in sim:
    mover = input("Deveria se mover?")
    if mover in sim:
        print("Sem problemas!")
    elif mover in nao:
        print("Silver tape")
    else:
        print("Resposta nao existe")