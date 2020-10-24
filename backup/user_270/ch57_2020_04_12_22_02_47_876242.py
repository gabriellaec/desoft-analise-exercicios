def verifica_progressao(l):
    for i in range(len(l)):
        pa = 0
        pg = 0
        pag = 0
        if l[i] == l[0] + (i-1)*(l[i+1]-l[i]) and l[i] ==l[0]*(l[i+1]/l[i])**(i-1):
            pag += 1
        elif l[i] == l[0] + (i-1)*(l[i+1]-l[i]) :
            pa += 1
        elif l[i] == l[0]*(l[i+1]/l[i])**(i-1):
            pg += 1
    if pag == len(l)-1 :
        return "AG"
    elif pa == len(l)-1 :
        return "PA"
    elif pg == len(l)-1 :
        return "PG"
    else:
        return "AN"
            