import math

def snell_descartes():
    n1 = int(input("Qual o valor de n1? ")) 
    n2 = int(input("Qual o valor de n2? ")) 
    teta1 = int(input("Qual o valor de θ1 (em graus)? "))
    
    teta1 = math.radians(teta1) 
    
    sen_teta1 = math.sin(teta1)
    
    sen_teta2 = (n1 * sen_teta1) / n2
    
    
    
    