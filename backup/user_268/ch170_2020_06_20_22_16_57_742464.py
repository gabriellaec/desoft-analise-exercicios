def apaga_repetidos(st):
    lit = []
    
    for i in st:
        if i in lit:
            st.replace(st[i], '*')
        else:
            lit.append(st[i])
            
    return st
        