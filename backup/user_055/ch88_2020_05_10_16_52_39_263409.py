class Retangulo:
    def __init__(self, cie, csd):
        self.cie = cie
        self.csd = csd

    def calcula_perimetro(self):
        a = self.csd.x - self.cie.x
        b = self.csd.y - self.cie.y
        return (a + b) * 2

    def calcula_area(self):
        a = self.csd.x - self.cie.x
        b = self.csd.y - self.cie.y
        return (a * b)