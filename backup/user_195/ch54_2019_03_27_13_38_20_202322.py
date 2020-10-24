def junta_nome_sobrenome(L,S):
    i=0
    F=[]
    while i<len(L):
        a="{0} {1}".format(L[i],S[i])
        F.append(a)
    	i+=1
    return F