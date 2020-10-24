class Retangulo:
    def __init__(self,p1,p2):
        self.inferior_esq=p1
        self.superior_direito=p2
        self.largura=self.superior_direito.x-self.inferior_esq.x
        self.comprimento=self.superior_direito.y-self.inferior_esq.y
    def calcula_perimetro(self):     
        return (2*self.largura+2*self.comprimento)
    def calcula_area(self):
        return (self.largura*self.comprimento)
        