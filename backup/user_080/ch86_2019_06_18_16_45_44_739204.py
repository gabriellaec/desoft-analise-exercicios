with open("dados.csv") as x:
    a=x.read()
    y = "".join(a).replace(',','\t')
    x.close()
with open("dados.tsv", "w") as z:
    h=z.write(y)
    
        