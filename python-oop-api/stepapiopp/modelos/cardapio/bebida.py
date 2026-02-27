from modelos.cardapio.item_cardapio import ItemCardapio

class bebida(ItemCardapio):
    # Conceito de Herança - A classe bebida herda os atributos nome e preco da classe ItemCardapio, além de adicionar um novo atributo tamanho.
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho