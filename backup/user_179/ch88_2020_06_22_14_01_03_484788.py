class Retangulo:
    def __init__(self, pie, psd):
        pie.x = Ponto(pie)
    def calcula_perimetro(self):
        dx = psd.x - self.x
        dy = psd.y - self.y
        return (dx*2 + dy*2)
    def calcula_area(self):
        dx = psd.x - self.x
        dy = psd.y - self.y
        return (dx*dy)