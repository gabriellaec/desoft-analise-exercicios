with open ('dados.csv','r') as arquivo:
    formatcsv = arquivo.read()
    formattsv= formatcsv.replace(','," ")
with open ('dados.tsv','w') as arquivo:
    arquivo.write(formattsv)