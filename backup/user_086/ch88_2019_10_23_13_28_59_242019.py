class Retangulo:
    def __init__(self,ponto1,ponto2):
        self.pontosupdir=ponto2
        self.pontoinfesq=ponto1
    def calcula_perimetro(self):
        per=abs(2*(pontosupdir.x-pontoinfesq.x))+abs(2*(pontoinfesq.y-pontosupdir.y))
        return per
    def calcula_area(self):
        area=abs(pontosupdir.x-pontoinfesq.x)*abs(pontoinfesq.y-pontosupdir.y)
        return area