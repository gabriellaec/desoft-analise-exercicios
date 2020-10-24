with open('dados.csv','r') as arquivo:
    t=arquivo.replace(',','') 
with open('dados.tsv','a') as arquivo:
    arquivo=t