with open('dados.csv', 'r') as arquivo:
    t = arquivo.read()
    t2 = t.replace(','," ")
    
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(t2)