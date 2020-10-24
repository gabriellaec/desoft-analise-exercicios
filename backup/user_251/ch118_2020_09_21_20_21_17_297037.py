import math
def reflexao_ou_refracao(n1,n2,o1):
    if n1 == 0:
        return "Índice de refração não pode valer zero"
    if n2 == n1:
        return False
    if n2 > n1:   
        seno_o2 = (n1/n2)*(math.sin(math.radians(o1)))
        if seno_o2 > 1:
            return True
        else:
            return False

        
print(reflexao_ou_refracao(2,1,45))


        
print(reflexao_total_interna(2,1,45))