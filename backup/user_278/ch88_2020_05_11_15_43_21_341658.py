class Ponto:
    def __init__ (self,valor_x,valor_y):
        self.x = x
        self.y = y
        
class Retangulo(Ponto):
    def __init__ (self,p1,p2):
        self.p_inf_esq = p1
        self.p_sup_dir = p2
        
    def calcula_perimetro (self):
        base = self.p_sup_dir.x - self.p_inf_esq.x
        alt = self.p_sup_dir.y - self.p_inf_esq.y
        p = 2*base + 2*alt
        return p
    
    def calcula_area (self):
        base = self.p_sup_dir.x - self.p_inf_esq.x
        alt = self.p_sup_dir.y - self.p_inf_esq.y
        a = base*alt
        return a