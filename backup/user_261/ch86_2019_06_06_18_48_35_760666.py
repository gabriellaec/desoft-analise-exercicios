with open("dados.csv",r) as arquivo and open('dados.tsv',w)as p:
    a=arquivo.read()
    b=a.replace(',','\t')
    c=p.write(b)
    
    
    