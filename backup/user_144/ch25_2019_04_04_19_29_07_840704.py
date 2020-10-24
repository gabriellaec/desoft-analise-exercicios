distância=float(input("Digite a distância a percorrer:"))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 100 + (distância - 200) * 0.45
    
print ("Preço da passagem R${0:.2f}".format(passagem))
      
      
    
