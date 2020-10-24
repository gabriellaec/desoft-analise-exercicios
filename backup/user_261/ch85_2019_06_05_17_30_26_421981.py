with open ("macacos-me-mordam.txt","r") as arquivo:
    a=arquivo.read()
    s=0
    a.replace("B","b")
    a.replace('A', 'a')
    a.replace('N',"n")
    for lines in a:
        if "banana"in lines:
            s+=1
print(s)
            
        
    
