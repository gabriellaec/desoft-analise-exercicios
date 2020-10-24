with open('dados.csv','r') as arquivo:
    t=arquivo.replace(',','	') 
with open('dados.tsv','r') as arquivo:
    arquivo=t