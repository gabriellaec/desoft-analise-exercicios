dic2={'p':111,'f':222,'q':333,'t':444,'e':555}
dic1={'e':123,'k':321,'t':231,'u':1332,'q':332}
def interseccao_chaves(dic1,dic2):
    lis_k=[]
    lis_k2=[]
    x=0
    for i in dic1.keys():
        lis_k.append(i)
    for e in dic2.keys():
        lis_k2.append(e)
    for i in lis_k:
        if i in lis_k2:
            del lis_k2[i]
    return lis_k2
