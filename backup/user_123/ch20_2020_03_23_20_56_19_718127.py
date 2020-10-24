a = float(input("Qual a distância que quer viajar?")
def preco(a):
	if a<=200 and a != 0:
          return (a*0.5)	
	else:
          return (40 +((a-200)*0.45))
          
print ("preco{0:.2f}".format(preco))

