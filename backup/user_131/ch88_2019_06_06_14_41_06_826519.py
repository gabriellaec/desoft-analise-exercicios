class Retangulo
    def __init__(self,ponto1, ponto2):
        self.x1 = ponto1
        self.y1 = ponto1
        
        self.x2 = ponto2
        self.y2 = ponto2
    def calcula_perimetro(self):
        p = 2*abs(self.x1 - self.x2) + 2*abs(self.y1 - self.y2)
    def calcula_area(sefl):
        a = abs(self.x1 - self.x2)*abs(self.y1 - self.y2)
    
    meu_numero = retangulo()
	meu_numero.calcula_perimetro()
    meu_numero.calcula_area()