def remove_palavra(palavra):
    x = palavra
    y = str()

    for i in x:
        if i != 'a':            
            if i != 'e':             
                if i != 'i':                
                    if i != 'o':                
                        if i != 'u':
                            y = y + i 
    return y
print(remove_palavra('babana'))