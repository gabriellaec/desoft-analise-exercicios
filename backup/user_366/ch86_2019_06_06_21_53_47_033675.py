with open("dados.csv", "r") as arquivo:
    a = arquivo.readlines()
    
    new = a.replace(',', ' ')
    
with open("dados.tsv", "w") as tsv:
    tsv.write(new)