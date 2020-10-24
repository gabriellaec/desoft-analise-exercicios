D=int(input("quanto vai? "))
def P(D)
    if D<=200:
        P=0.5*D
        return P
    else:
        P=0.45*D
        return P
print("o preço é R$ {0:.2f}".format(P))