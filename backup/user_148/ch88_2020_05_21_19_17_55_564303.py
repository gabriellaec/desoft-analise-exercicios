class Retangulo:
    def __init__(self, inf_esq, sup_dir):
        self.inf_esq = inf_esq
        self.sup_dir = sup_dir
        
    def calcula_perimetro(self):
        a = self.sup_dir.x - self.inf_esq.x
        b = self.sup_dir.y - self.inf_esq.y
        return 2*(a+b)
    
    def calcula_area(self):
        c = self.sup_dir.x - self.inf_esq.x
        d = self.sup_dir.y - self.inf_esq.y
        return c*d
