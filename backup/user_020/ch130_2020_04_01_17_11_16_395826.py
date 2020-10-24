mala = []
def monta_mala(y):
    while sum(mala) <= 23:
        x = int(input("Insira o peso da sua bagagem"))
        if x <= 23:
            mala.append(x)
        else:
            print("Você não pode colocar bagagens acima de 23kg")
