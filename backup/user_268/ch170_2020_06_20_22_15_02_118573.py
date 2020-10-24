def apaga_repetidos(st):
    lit = []
    
    for i in range (len(st)):
        if st[i] in lit:
            st.replace(st[i], '*')
        else:
            lit.append(st[i])
            
    return st
        