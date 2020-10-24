def verifica_lista(l):
    p = False
    i = False
    for i in l:
        if i % 2 == 0:
            p = True
        else:
            i = True
    if p and i == True:
        print("misturado")
    elif p == True:
        print("par")
    else:
        print("ímpar")