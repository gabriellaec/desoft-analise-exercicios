class Retangulo:
    def __init__ (self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def calcula_perimetro (self):
        largura = p1.x - p2.x
        if largura < 0:
            largura = -1*largura
        altura = p1.y - p2.y
        if altura < 0 :
            altura = -1*altura
            
        perimetro = 2*(largura + altura)
        return perimetro
        
    def calcula_area (self):
        area = largura*altura
        
        return area
        