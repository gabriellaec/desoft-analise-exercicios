class Retangulo:
    def __init__(self,p1,p2):
        self.inferior_esq=p1
        self.superior_direito=p2
    def calcula_perimetro(self):
        self.x_esq=self.inferior_esq.x
        self.y_esq=self.inferior_esq.y
        self.x_dir=self.superior_direito.x
        self.y_dir=self.superior_direito.y
        return (2*(self.x_dir-self.x_esq)+(2*(self.y_dir-self.y_esq)))
    def calcula_area(self):
        self.x_esq=self.inderior_esq.x
        self.y_esq=self.inderior_esq.y
        self.x_dir=self.superior_direito.x
        self.y_dir=self.superior_direito.y
        return ((self.x_dir-self.x_esq)*(self.y_dir-self.y_esq))
        