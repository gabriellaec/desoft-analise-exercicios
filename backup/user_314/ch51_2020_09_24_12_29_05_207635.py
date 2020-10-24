def primos_entre (a,b):
    lista=[]
    i=a

    while(i<b-a+1):
        if(primo(i)== True):
            lista.append(i)
        i+=1  

    return lista

def primo(num):
    c=0
    if(num==2):
        return True
  
    elif(num<2):
        return False
  
    else:
        for i in range(2,num):
            if(num%i==0):
                c+=1
    
    if(c!=0):
        return False
    else:
        return True
