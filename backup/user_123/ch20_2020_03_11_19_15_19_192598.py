a = input("Qual a distância que quer viajar?")
def preco(a):
    if a<=200:
        return a*0.5
    else:
        return 40 +((a-200)*0.45)    
print (preco)