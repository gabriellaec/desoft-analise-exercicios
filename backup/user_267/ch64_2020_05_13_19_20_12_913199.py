def acha_bigramas(s):
    todos_bi = []
    for i in range(0, len(s)-1):
        if (s[i]+s[i+1]) not in todos_bi:      
            todos_bi.append(s[i]+s[i+1])
    return todos_bi

                     