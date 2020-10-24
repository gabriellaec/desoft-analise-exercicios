import math

class Retangulo:
    def __init__(self, inf_esq, sup_dir):
        self.inf_esq=inf_esq
        self.sup_dir=sup_dir
	    
    def calcula_area(self):
        return math.sqrt(((self.inf_esq.x-self.sup_dir.x)**2)+((self.inf_esq.y-self.sup_dir.y)**2))
    
    def calcula_perimetro(self):
        return 2*(self.inf_esq.x-self.sup_dir.x)+2*(self.inf_esq.y-self.sup_dir.y)
    
    