class Retangulo:
    def calcula_perimetro(self, ponto2):
        dx = ponto2.x - self.x
        dy = ponto2.y - self.y
        return ((dx*2)+(dy*2))
    def calcula_area(self, dx, dy):
        a = dx*dy
        return a
       
        
       