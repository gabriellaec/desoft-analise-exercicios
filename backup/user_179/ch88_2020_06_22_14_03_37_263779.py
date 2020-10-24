class Retangulo:
    def __init__(self, pie, psd):
        self.pie = pie
        self.psd = psd
        self.dx = self.psd.x - self.pie.x
        self.dy = self.psd.y - self.pie.y
    def calcula_perimetro(self):
        return (dx*2 + dy*2)
    def calcula_area(self):
        return (dx*dy)