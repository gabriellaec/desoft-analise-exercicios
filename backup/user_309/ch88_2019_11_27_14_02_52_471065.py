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
    