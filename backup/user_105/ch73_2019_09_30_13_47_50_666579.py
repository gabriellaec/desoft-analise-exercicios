def remove_palavra(palavra):
    x = str(palavra)
    y = str()

    for i in range(len(x)):
        if i != 'a':            
            if i != 'e':             
                if i != 'i':                
                    if i != 'o':                
                        if i != 'u':
                            y = y + i 
    return y
print(remove_palavra(babana))