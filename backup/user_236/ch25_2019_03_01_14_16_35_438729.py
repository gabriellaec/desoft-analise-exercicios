D=int(input("quanto vai? "))
def P(D)
    if D<=200:
        P=0.5*D
        return P
    else:
        P=200*0.5+0.45*(D-200)
        return P
print("o preço é R$ {0:.2f}".format(P))