def eh_primo (x):
    if x==0 or x==1:
        return False
    elif x % 2 == 0 and x!=2:
        return False
    else:
        z= 1
        y= 2*z+1
        while y < x:
            if x%y==0: 
                return False
                break
            else:
                z = z + 1
        if x==y:
            return True