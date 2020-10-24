class Retangulo:

    def __init__(self, _ponto1, _ponto2):
        self.ponto1 = _ponto1
        self.ponto2 = _ponto2
    
    def calcula_perimetro(self):
        lado1 = self.ponto1.x - self.ponto2.x
        lado2 = self.ponto1.y - self.ponto2.y
        perimetro = (2*lado1) + (2*lado2)
        return perimetro

    def calcula_area(self):
        lado1 = self.ponto1.x - self.ponto2.x
        lado2 = self.ponto1.y - self.ponto2.y
        area = lado1 * lado2
        return area