a = int(input('Escreva um ano aleatório, e lhe direi se este é bissexto'))
if a%4 == 0 and a%100 != 0:
    return True    
elif a%400 == 0 and a%100 ==0:
    return True
else:
    return False
     
   
        
        
   