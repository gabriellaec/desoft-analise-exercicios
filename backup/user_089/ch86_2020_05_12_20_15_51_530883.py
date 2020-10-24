with open("dados.csv","r") as arquivo:
    x = arquivo.read()
    i = []
    y = x.split(",")
    for e in y:
        i.append(y+"\t")
print(i)
    