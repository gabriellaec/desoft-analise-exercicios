with open('dados.csv','r') as arquivo:
    a=arquivo.read()
    b=a.replace(',','	')
with open('dados.tsv','r') as arquivo:
    arquivo.write(b)