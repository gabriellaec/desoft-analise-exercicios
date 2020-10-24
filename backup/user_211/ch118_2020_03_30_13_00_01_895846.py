import math
def reflexao_total_interna(n1,n2,teta2):
	if(n2>n1):
		if(math.sin(teta2)>91):
			return True
        else:
            return False
    
	else:
		return False


print(reflexao_total_interna(1,1,30))