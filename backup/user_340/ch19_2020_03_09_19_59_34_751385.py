def classifica_triangulo(L1,L2,L3):
    if L1==L2 and L2==L3:
    	return 'equilatero'
    if L1==L2 and L2!=L3:
        return 'isoceles'
    if L1!=L2 and L2!=L3:
        return 'escaleno'
    
    	
    
    