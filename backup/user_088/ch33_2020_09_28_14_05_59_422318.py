def primos_entre(a,b):
    i = a
    while i<=b:
        if primos_entre(a,b) == True:
               b-=i
            i+=1
    return len(i)