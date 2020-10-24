def quantos_uns(x):
    y= str(x)
    a= 0
    b= 0
    while a < len(y):
        if y[a] == "1":
            b= b + 1
        a= a + 1
    return b
           
    