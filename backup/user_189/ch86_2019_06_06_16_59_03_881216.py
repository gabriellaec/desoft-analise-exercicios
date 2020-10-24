open('dados.csv','r') as csv:
	texto= csv.read()
tx=(','.join(texto))
end=csv.read(tx)
close('dados.csv')
    