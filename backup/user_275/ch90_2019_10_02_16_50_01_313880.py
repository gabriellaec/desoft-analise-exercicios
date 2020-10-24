def segundos_entre(T1,T2):
    s1=int(T1[6:8])
    s2=int(T2[6:8])
    m1=int(T1[3:5])
    m2=int(T2[3:5])
    h1=int(T1[0:2])
    h2=int(T2[0:2])
    S1=s1+(m1*60)+(h1*3600)
    S2=s2+(m2*60)+(h2*3600)
    diferenca=S2-S1
    return diferenca