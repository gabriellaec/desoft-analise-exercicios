class Retangulo:
    """ Classe que representa um Retângulo. """
    def __init__(self, p1, p2):
        #ponto inferior esquerdo
        self.p1 = p1
        #ponto superior direito 
        self.p2 = p2
    
    def calcula_perimetro(self):
        a = self.p1.x - self.p1.x
        b = self.p2.y - self.p2.y
        return 2 * (a + b)
    
    def calcula_area(self):
        a = self.p1.x - self.p1.x
        b = self.p2.y
        return a*b