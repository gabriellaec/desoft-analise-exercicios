def conta_bigramas(s):
    dici={}
    li=[]
    s1=s[0]
    s2=s[1]
    soma= s1+s2
    li.append(soma)
    for s1 in range(2, len(s)):
        soma=s2+s[s1]
        li.append(soma)
        s2=s[s1]
    i=0
    while i<len(li):
        b=0
        c=0
        while b<len(li):
            if li[i]==li[b]:
                c+=1
                b+=1
            else:
                b+=1
        dici[li[i]]=c
        i+=1
    return dici
        