def aniversariantes_de_setembro(niver):
    dic={}
    for n,a in niver.items():
        if a[3]==0 and a[4]==9:
            dic[n]=a
    return dic