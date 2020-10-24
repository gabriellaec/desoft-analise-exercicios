class Retangulo:
    
    def __init__(self, _ponto1, _ponto2):
        self.p1 = _ponto1
        self.p2 = _ponto2
    def calcula_perimetro(self):
        h = self.p2.x - self.p1.x
        b = self.p2.y - self.p1.y
        per = (2*h) + (2*b)
        return per
    def calcula_area(self):
        h = self.p2.x - self.p1.x
        b = self.p2.y - self.p1.y
        area = h*b
        return area