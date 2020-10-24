s=0
with open ('macacos-me-mordam.txt',"r") as arquivo:
    a=arquivo.read()
    c=a.lower()
    b=c.split()
    for palavras in b:
        if palavras== "banana":
            s+=1
print(s)
            
          
        
    
