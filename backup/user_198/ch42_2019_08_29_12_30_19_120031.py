def quantos_uns(num)
	cont=0
    aux=0
    while num>=0:
        aux=num%10
        if aux==1:
            cont+=1
        num=(num-aux)/10
    return(cont)
    
    