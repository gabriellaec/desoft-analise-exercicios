class Retângulo:
    def __init__(self, ponto_inf_esq, ponto_sup_dir):
        self.esq = [ponto_inf_esq.x, ponto_inf_esq.y]
        self.dir = [ponto_sup_dir.x, ponto_sup_dir.y]
    def calcula_perimetro(self):
        horiz = ponto_sup_dir.x - ponto_inf_esq.x
        vert = ponto_sup_dir.y - ponto_inf_esq.y
        perimetro = 2*(horiz+vert)
        return perimetro
    def calcula_area(self)
        horiz = ponto_sup_dir.x - ponto_inf_esq.x
        vert = ponto_sup_dir.y - ponto_inf_esq.y
        area = horiz*vert
        return area