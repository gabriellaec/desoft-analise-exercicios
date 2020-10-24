class Ponto:
    def __init__(self,valor_x,valor_y):
        self.x = valor_x
        self.y = valor_y
        
class Retangulo(Ponto):
    def __init__(self, ponto1, ponto2):
        self.p_inf_esq = ponto1 #ponto do canto inferior esquerdo
        self.p_sup_dir = ponto2 #ponto do canto superior direito

    def calcula_perimetro(self):
        altura = self.p_sup_dir.y - self.p_inf_esq.y
        base = self.p_sup_dir.x - self.p_inf_esq.x
        p = 2*altura + 2*base
        return p
    
    def calcula_area(self):
        altura = self.p_sup_dir.y - self.p_inf_esq.y
        base = self.p_sup_dir.x - self.p_inf_esq.x
        a = base*altura
        return a
