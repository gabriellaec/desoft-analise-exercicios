def remove_vogais(st):
    vog = ['a', 'e', 'i', 'o' , 'u']
    for i in vog:
        if i in st:
            st.remove(i)
    return st