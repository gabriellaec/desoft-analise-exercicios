class Carrinho:
  def _init_(self):
        di ={}
        self.dicionario = di

  def adiciona(self, nome_produto, preco):
    if nome_produto not in self.dicionario:
      self.dicionario[nome_produto]=preco
    else:
      self.dicionario[nome_produto] += preco

  def total_do_produto(self, nome_produto):
    return self.dicionario[nome_produto]