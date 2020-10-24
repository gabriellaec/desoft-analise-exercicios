def eh_primo(x):
    primo = True
    if (x%2==0 and x!=2) or (x==1):
    primo = False
    i = 2
    while (i<x):
        if i%2!=0:
            if n%i==0:
                primo = False
        i+=1
        if primo == True:
            return True
        else:
            return False
print (eh_primo(0))
            

    
    


    