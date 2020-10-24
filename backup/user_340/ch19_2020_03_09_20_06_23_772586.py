def classifica_triangulo(L1,L2,L3):
    if L1==L2 and L2==L3:
    	return "equilátero"
    if L1==L2 and L2!=L3:
        return "isósceles"
    if L1!=L2 and L1==L3:
        return "isósceles"
    if L1!=L2 and L2==L3:
        return "isósceles"
    if L1!=L2 and L2!=L3:
        return "escaleno"

    
    	
    
    