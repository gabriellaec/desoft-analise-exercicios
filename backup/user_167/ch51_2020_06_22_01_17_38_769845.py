def  primos_entre (a,b):
    i=b
    while i > a:
        if i < 2:
            return False
        elif i == 2:
            return True
        elif i % 2 == 0:
            return False
        else:
            l=3
            while i < l:
                if i % l == 0:
                    return False
                l+=2
        i -=1
            
            