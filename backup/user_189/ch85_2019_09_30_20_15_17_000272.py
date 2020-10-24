def lots_of_bananas():
    
    contador=0
    
    with open("macacos-me-mordam.txt", 'r') as file:
        file = file.upper()
        for a in file:
            if a == "BANANA":
                contador+=1
            
  	return contador


    
    
    