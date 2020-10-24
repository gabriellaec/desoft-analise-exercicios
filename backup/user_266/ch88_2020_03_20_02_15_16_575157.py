class Retangulo:
    def __init__(self, ponto1, ponto):
        self.ponto1 = ponto1
        self.ponto = ponto
    def calcula_perimetro(self):
        return 2*(abs(ponto.y - ponto1.y)) + 2*(abs(ponto.x - ponto1.x))
    def calcula_area(self):
        return abs(ponto.y - ponto1.y) * abs(ponto.x - ponto1.x)