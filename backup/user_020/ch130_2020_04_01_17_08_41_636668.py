mala = []
def monta_mala():
    x = int(input("Insira o peso da sua bagagem"))
    if x <= 23:
        mala.append(x)
    else:
        print("Você não pode colocar bagagens acima de 23kg")
