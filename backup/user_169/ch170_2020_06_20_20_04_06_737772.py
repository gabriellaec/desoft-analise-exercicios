def apaga_repetidos(string):
   
    soma=''
    for i in string:
        if i not in soma:
            soma+=i

        else:
            soma+='*'         

    return soma
        
        
        