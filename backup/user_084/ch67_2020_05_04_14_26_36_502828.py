def alunos_impares(l):
    s=l.split()
    print(s)
    imp=[]
    i=1
    while i<len(s):
        imp.append(s[i])
        i+=2
    return imp