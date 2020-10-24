def PiWallis (n):
    produto=2/1
    cont=2
    num=2
    den=1
    while cont < n:
        if n==1:
            break
        else:
            den+=2
            produto=produto*num/den
            cont+=1
            if cont > n:
                break
            num += 2
            produto=produto*num/den
            cont+=1
    pi=2*produto
    return pi
    


            
        
        
        