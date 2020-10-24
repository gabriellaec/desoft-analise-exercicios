def remove_vogais(string):
    palavra=string
    i=0
    while i <= len(palavra):
        if palavra[i]=="a":
           delete palavra[i]
        if palavra[i]=="e":
           delete palavra[i]    
		if palavra[i]=="i":
           delete palavra[i]
        if palavra[i]=="o":
           delete palavra[i]
        if palavra[i]=="u":
           delete palavra[i]
        i=1+i                 
    return palavra               