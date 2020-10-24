with open('dados.csv','r') as arquivo:
    a=arquivo.read() 
    a.split('    ')
with open('dados.tsv','r') as arquivo2:
    b=arquivo2.read()
    b.writelines(a)
    print(b)
