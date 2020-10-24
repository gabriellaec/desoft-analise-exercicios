with open('dados.csv','r') as arquivo:
    t=arquivo
    t=t.replace(',','') 
with open('dados.tsv','a') as arquivo:
    arquivo=t