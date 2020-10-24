def pos_arroba(x):
    
    i = 0 
    while i < len(x):
        if x[i] == "@":
            return i 
        i += 1
        
    
        
        
print(pos_arroba("murilo@menezes.org"))