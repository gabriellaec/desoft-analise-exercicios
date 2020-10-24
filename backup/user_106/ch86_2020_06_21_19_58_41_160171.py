with open ('dados.csv','r') as arq:
    cont=arq.read()

tsv=cont.replace(',','	')

with open ('dados.tsv','w') as arqui:
    arqui.write(tsv)