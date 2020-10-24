f=[]
a=input("palavra")
while a!="fim":
    if a[0]=="a":
        f.append(a)
    a=input("palavra")
i=0    
while i<len(f):
    print(f[i])
    i+=1
        
              