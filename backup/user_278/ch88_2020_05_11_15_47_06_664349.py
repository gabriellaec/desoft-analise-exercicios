class Ponto:
    def __init__(self, valor_x, valor_y):
        self.x = valor_x
        self.y = valor_y
        
class Retangulo(Ponto):
    def __init__ (self, p1, p2):
        self.p_inf_esq = p1
        self.p_sup_dir = p2
    
    def calcula_perimetro (self):
        alt = self.p_sup_dir.y - self.p_inf_esq.y
        base = self.p_sup_dir.x - self.p_inf_esq.x
        p = 2*alt + 2*base
        return p
    
    def calcula_area (self):
        alt = self.p_sup_dir.y - self.p_inf_esq.y
        base = self.p_sup_dir.x - self.p_inf_esq.x
        a = alt*base
        return a

