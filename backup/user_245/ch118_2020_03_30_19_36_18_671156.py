import math
def reflexao_total_interna(n1,n2,t2):
    #funcao que retorna verdadeiro caso haja uma reflexao interna total
    #funcao que retorna falso caso seja uma refracao   
    limite = math.degrees(math.asin(math.radians(n2/n1)))
    if t2>limite:
        reflexao_total = True
        return reflexao_total
    else:
        reflexao_total = False
        return reflexao_total
