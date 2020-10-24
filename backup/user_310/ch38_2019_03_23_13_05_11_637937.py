def primos_entre(a, b):
    
    quantidade_primos=0
    
    a=a
    i=2
    while a<=b:
       if a<=1:
           a+=1
       if a%i!=0:
           quantidade_primos+=1
    
       a+=1
    
    return quantidade_primos