class Retangulo:
    
    def __init__(self, p1, p2):
        self.pie = p1
        self.psd = p2
    
    def distancia(self):
        subx = (self.psd.x - self.pie.x)**2
        suby = (self.psd.y - self.pie.y)**2

        return math.sqrt(subx + suby)
    
    def calcula_perimetro(self):
        eixoX = self.psd.x - self.pie.x
        eixoY = self.psd.y - self.pie.y

        return (2*eixoX) + (2*eixoY)
    
    def calcula_area(self):
        eixoX = self.psd.x - self.pie.x
        eixoY = self.psd.y - self.pie.y
    
        return eixoX * eixoY