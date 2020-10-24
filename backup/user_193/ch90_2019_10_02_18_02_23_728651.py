def segundos_entre(s1, s2):
    h1=int(s1[0]+s1[1])*3600
    m1=int(s1[3]+s1[4])*60
    s1=int(s1[6]+s1[7])
    h2=int(s2[0]+s2[1])*3600
    m2=int(s2[3]+s2[4])*60
    s2=int(s2[6]+s2[7])
    hr1=h1+m1+s1
    hr2=h2+m2+s2
    return hr2-hr1