class Retangulo:
    def __init__(self,inf_esquerdo,sup_direito):
        self.inf_esq = inf_esquerdo
        self.sup_dir = sup_direito
    
    def calcula_perimetro(self,b,h):
        perimetro = 2*(b+h)
        return perimetro
        
        
    def calcula_area(self,b,h):
        area = b * h
        return area


# Programa Principal    
p1 = Retangulo(5,4)
p2 = Retangulo(3,2)
    
perim = p1.calcula_perimetro(10,4)
area = p1.calcula_area(5,2)
    
print('perim:{0},area:{1}'.format(perim,area))