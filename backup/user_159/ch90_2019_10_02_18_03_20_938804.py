def segundos_entre(x,z):
    x1=int(x[0,1])
    x2=int(x[3,4])
    x3=int(x[6,7])
    xs=(x1*3600)+(x2*60)+x3
    
    z1=int(x[0,1])
    z2=int(x[3,4])
    z3=int(x[6,7])
    zs=(z1*3600)+(z2*60)+z3
    
    s=zs-xs
    return s
