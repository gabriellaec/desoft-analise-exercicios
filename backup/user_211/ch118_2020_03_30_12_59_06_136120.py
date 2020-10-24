import math
def reflexao_total_interna(n1,n2,teta2):
    if(n2>n1):
        if(math.sin(teta2)>91):
            True
        else:
            False
    
	else:
        False


print(reflexao_total_interna(1,1,30))