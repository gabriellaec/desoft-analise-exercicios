class Retangulo():
    def __init__(self, _ponto1, _ponto2):
        self.inf_esq = _ponto1
        self.sup_di = _ponto2
        
    def calcula_perimetro(self):
        self.base = self.sup_di.x - self.inf_esq.x
        self.altura = self.sup_di.y - self.inf_esq.y 
        
        self.perimetro = self.altura*2 + self.base*2
        return seld.perimetro
    
    def calcula_area(self):
        self.area = self.base*self.altura 
        return self.area 