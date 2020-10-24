primeira_p = input("Está funcionando? (n/s) ")
if primeira_p == "s":
    print("Sem problemas!")
else:
    segunda_p = input("você sabe corrigir? (s/n) ")
    if segunda_p == "s":
        print("Sem problemas!")
    else:
        terceira_p = input("Você precisa corrigir? (s/n) ")
        if terceira_p == "n":
            print("Sem problemas!")
        else:
            print("Apague tudo e tente novamente")