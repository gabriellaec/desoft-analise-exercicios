class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.pontoinfesq = ponto1
        self.pontosupdir = ponto2
        
    def calcula_perimetro(self):
        a = self.pontosupdir.x - self.pontoinfesq.x
        b = self.pontosupdir.y - self.pontoinfesq.y
        return 2*(a+b)
    
    def calcula_area(self):
        a = self.pontosupdir.x - self.pontoinfesq.x
        b = self.pontosupdir.y - self.pontoinfesq.y
        return (a*b)