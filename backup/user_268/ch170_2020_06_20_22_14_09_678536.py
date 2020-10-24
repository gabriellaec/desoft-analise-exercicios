def apaga_repetidos(st):
    lit = []
    
    for i in st:
        if i in lit:
            st.replace(i, '*')
        else:
            lit.append(i)
            
    return st
        