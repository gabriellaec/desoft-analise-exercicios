class Retangulo:
    
    def __init__ (self, p1, p2):
        self.ie = p1
        self.sd = p2
        
    def perimetro(self):
        a = self.sd.x - self.ie.x
        b = self.sd.y - self.ie.y
        return 2 * (a + b)