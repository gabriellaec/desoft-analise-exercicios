with open('dados.csv','r') as arquivo:
    t=arquivo.read()
    t=t.split(',') 
    t2=('	').join(t)
with open('dados.tsv','w') as arquivo:
    arquivo.write(t2)