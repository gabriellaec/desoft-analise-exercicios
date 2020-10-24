with open("churras.txt", "r") as arquivo:
    total=0
    conteudo=arquivo.readlines()
    for i in conteudo:
        a=i.split(,)
        total+=int(a[1]) * float(a[2])
print(total)
            