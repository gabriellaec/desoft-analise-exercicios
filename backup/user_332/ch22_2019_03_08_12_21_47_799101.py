def eh_bissexto (ano):
    if(ano%4 == 0):
        return(True)
    elif(ano%400 != 0 and ano%100 == 0):
        return(False)
    else:
        return(False)
    
