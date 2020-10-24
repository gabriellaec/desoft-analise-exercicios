def aniversariantes_de_setembro(n):
    dic={}
    for y,a in n.items():
        if a[3]=='0':
            if a[4]=='9':
                dic[y]=a
    return dic