def remove_vogais(x):
    for i in range(0,len(x)):
        if x[i] =="a" or x[i] =="e" or x[i] == "i" or  x[i] =="o" or x[i] =="u":
            string = x[1:i] + x[i+1:len(x)]
    return string
        
        
    
	
            
