i=True
x=("Sem problemas!")
while i==True:
    p1=input("esta funcionando? ")
    if p1=="s":
        print(x)
        i=False
    elif p1== "n":
        p2=input("voce sabe corrigir? ")
        if p2=="s":
            print(x)
            i=False
        elif p2== "n":
            p3=input("voce precisa corrigir? ")
            if p3 == "s":
                print("apague tudo e tente novamente")
                i=False
            elif p3== "n":
                print(x)
                i=False
