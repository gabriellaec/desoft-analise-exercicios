def quantos_uns (num):
    contador=0
    while (num>9):
        a=num%10
        num=num//10

        if(a==1):
            contador+=1
     
    if(num==1):
        contador+=1

    return contador