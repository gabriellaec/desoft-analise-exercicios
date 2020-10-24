n=int(input("digite a distancia em km:"))
    
if n <= 200:
    passagem = (n*0.5)
else:
    passagem = (((n-200)*0.45)+100)

    
print(passagem)