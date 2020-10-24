class Retangulo:
    def __init__(self,P1,P2):
        self.x = P1
        self.y = P2
        print(self.x)
        
    def calcula_perimetro(self):
        altura = self.y.y - self.x.y
        comprimento = self.y.x - self.x.x
        return 2*(comprimento+altura)
    def calcula_area(self):
        altura = self.y.y - self.x.y
        comprimento = self.y.x - self.x.x
        return comprimento*altura
        
        