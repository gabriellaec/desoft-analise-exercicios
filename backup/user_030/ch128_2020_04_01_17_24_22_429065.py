sim = ["sim", "s"]
nao = ["nao", "n", "não"]

movendo = input("Esta se movendo?")
if movendo in nao:
    deveparado = input("Deveria estar parado?")
    if deveparado in sim:
        print("Sem problemas!")
    elif deveparado in nao:
        print("WD-40")
    else:
        print("Resposta nao existe")
if movendo in sim:
    devemover = input("Deveria se mover?")
    if devemover in sim:
        print("Sem problemas!")
    elif devemover in nao:
        print("Silver tape")
    else:
        print("Resposta nao existe")