def verifica_progressao(s):
    i=1
    PA=[]
    PG=[]
    while i<= len(s)-1:
    	rpa=s[i]-s[i-1]
        PA.append(rpa)
   		rpg=s[i]/s[i-1]
        PG.append(rpg)
        i+=1
    n=1
    while n <=len(PA)-1:
        pg=True
        pa=True
        if PA[n] != PA [n-1]:
        	pa=False
        
        if PG[n] != PG [n-1]
        	pg=False
            
        n+=1
    if pa and pg:
        return "AG"
    elif pa:
        return "PA"
    elif pg:
        return "PG"
    else:
        return "NA"
            
        