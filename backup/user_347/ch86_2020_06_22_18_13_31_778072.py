with open ("dados.csv", "r") as csv:
    ler = csv.read()
    x = ler.split()
    for i in x:
        if i == ",":
            i.replace("	")
with open ("dados.tsv", "w") as tsv:
    print("").join(x) 
    esc = tsv.write(a)
            