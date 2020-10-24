def remove_vogais(st):
    vog = ['a', 'e', 'i', 'o' , 'u']
    a = st
    for i in vog:
        if i in st:
             a = a.replace(i,"")
    return a