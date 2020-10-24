def segundos_entre(s1,s2):
    h = int(s1[0:2])
    
    h1 = h*3600
    m = int(s1[4:6])
    m1 = m * 60
    s = int(s1[7:9])
    
    t1 = s + m1 + h1
    
    H = int(s1[0:2])
    H1 = H*3600
    M = int(s1[4:6])
    M1 = M * 60
    S = int(s1[7:9])
    
    t2 = H1 + M1 + S
    
    return t2 - t1
    