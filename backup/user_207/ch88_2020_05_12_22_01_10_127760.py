class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo:
    def __init__ (self, ponto_inf, ponto_sup): #a função retangulo receberá 2 pontos
        self.p1 = ponto_inf
        self.p2 = Ponto(ponto_sup.x, ponto_inf.y)
        self.p3 = ponto_sup
        self.p4 = Ponto(ponto_inf.x, ponto_sup.y)


    def calcula_perimetro (self):
        dx = self.p2.x - self.p1.x
        dy = self.p3.y - self.p2.y
        perimetro = 2*(dx + dy)

        return perimetro

    def calcula_area (self):
        dx = self.p2.x - self.p1.x
        dy = self.p3.y - self.p2.y
        area = dx*dy

        return area