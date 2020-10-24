
class Ponto:
    '''Classe representa um ponto.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self,p1,p2):
        self.inf_esq = p1
        self.sup_dir = p2
    def calcula_perimetro(self):
        a = self.sup_dir.x - self.inf_esq.x
        b = self.sup_dir.y - self.inf_esq.y
        return 2*(a+b)
    def calcula_area(self):
        a = self.sup_dir.x - self.inf_esq.x
        b = self.sup_dir.y - self.inf_esq.y
        return a*b
