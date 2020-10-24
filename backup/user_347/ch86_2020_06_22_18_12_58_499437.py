with open ("dados.csv", "r") as csv:
    ler = csv.read()
    x = ler.split()
    for i in x:
        if i == ",":
            i.replace("	")
with open ("dados.tsv", "w") as tsv:
    a = x.join() 
    esc = tsv.write(a)
            