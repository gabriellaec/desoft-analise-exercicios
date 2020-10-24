with open('dados.csv','r') as arquivo:

	b=a.replace(',','	')
with open('dados.tsv','w') as arquivo:
    arquivo.write(b)