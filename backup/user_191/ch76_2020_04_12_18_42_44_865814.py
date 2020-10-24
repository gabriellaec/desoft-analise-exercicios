def aniversariantes_de_setembro(n):
    dic={}
    for n,a in n.items():
        if a[3]==0:
            if a[4]==9:
                dic[n]=a
    return dic