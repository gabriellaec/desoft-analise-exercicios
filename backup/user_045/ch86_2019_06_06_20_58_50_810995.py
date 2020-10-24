with open('dados.csv','r') as arquivo:
    t=arquivo.read()
    t=t.split(',') 
    t=t.join('	')
with open('dados.tsv','w') as arquivo:
    arquivo=t