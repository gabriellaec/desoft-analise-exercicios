class Retangulo:
    def __init__(self,p1,p2):
        self.p1x=p1x
        self.p1y=p1y
        self.p2x=p2x
        self.p2y=p2y
    def calcula_perimetro(self):
        ldx=(self.p2x-self.p1x)
        ldy=(self.p2y-self.p1y)
        perimetro=(ldx+ld2)*2
        return perimetro
        
    def calcula_area(self):
        ldx=(self.p2x-self.p1x)
        ldy=(self.p2y-self.p1y)
        area=ldx*ldy
        return area