class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
    def calcula_perimetro(self):
        return 2*(abs(ponto1.y - ponto2.y)) + 2*(abs(ponto1.x - ponto2.x))
    def calcula_area(self):
        return abs(ponto1.y - ponto2.y) * abs(ponto1.x - ponto2.x)