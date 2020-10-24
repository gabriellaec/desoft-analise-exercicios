class Retangulo:
    def __init__(self, ponto_inf_esq, ponto_sup_dir):
        self.esq = [ponto_inf_esq.x, ponto_inf_esq.y]
        self.dir = [ponto_sup_dir.x, ponto_sup_dir.y]
    def calcula_perimetro(self):
        horiz = self.dir[0] - self.esq[0]
        vert = self.dir[1] - self.esq[1]
        perimetro = 2*(horiz+vert)
        return perimetro
    def calcula_area(self):
        horiz = self.dir[0] - self.esq[0]
        vert = self.dir[1] - self.esq[1]
        area = horiz*vert
        return area