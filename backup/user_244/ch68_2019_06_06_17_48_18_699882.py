def separa_trios(x):
   
    a = [] 
    b = []
    c = []
    
    for i in range(len(x)):
        a.append(x[0:3])
        b.append(x[3:6])
        c.append(x[6:len(x)])
        return [a, b , c]
        

 


               