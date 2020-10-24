def junta_nomes(M,F,S):
    if len(M)==0 and len(F) == 0:
        return []
    elif S==[]:
        return []
    else:
        lista=[]
        for i in range(len(M)):
            for j in range(len(S)):
                N=M[i]+" "+S[j]
                lista.append(N)
        for i in range(len(F)):
            for j in range(len(S)):
                N1=F[i]+" "+S[j]
                lista.append(N1)
        return lista