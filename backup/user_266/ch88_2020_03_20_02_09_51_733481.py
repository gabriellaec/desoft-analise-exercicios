class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def calcula_perimetro(self):
        return 2*(abs(ponto2.y - ponto1.y)) + 2*(abs(ponto2.x - ponto1.x))
    def calcula_area(self):
        return abs(ponto2.y - ponto1.y) * abs(ponto2.x - ponto1.x)