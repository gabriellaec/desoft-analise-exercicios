import math
def reflexao_total_interna(n1,n2,o1):
    if n2 == 0:
        return "Índice de refração não pode valer zero"
    if n1 == n2:
        return False
    if n1 > n2:   
        seno_o2 = (n1/n2)*(math.sin(math.radians(o1)))
        if seno_o2 > 1:
            return True
        else:
            return False

        
print(reflexao_total_interna(2,1,45))