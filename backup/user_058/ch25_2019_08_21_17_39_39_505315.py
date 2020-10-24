
x = int(input("Qual a distância que você irá percorrer? ")

def preço(x):
    if (x<=200):
        p= x*0.50
        return p
	else (x>200):
        r= (200*0.50)+((x-200)*0.45)
		return r
print (x)