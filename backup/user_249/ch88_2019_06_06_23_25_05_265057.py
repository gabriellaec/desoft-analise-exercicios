class Retangulo:
   
    def calcula_perimetro(self):
        ldx=(self.p2x-self.p1x)
        ldy=(self.p2y-self.p1y)
        perimetro=(ldx+ldy)*2
        return perimetro
        
    def calcula_area(self):
        ldx=(self.p2x-self.p1x)
        ldy=(self.p2y-self.p1y)
        area=ldx*ldy
        return area