from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    # Conceito de Herança - A classe bebida herda os atributos nome e preco da classe ItemCardapio, além de adicionar um novo atributo tamanho.
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} - {self._tamanho} - R${self._preco:.2f}'
    ## O método __str__ é um método especial em Python que é chamado quando um objeto é convertido para uma string, como quando é impresso. Ele é usado para definir a representação em string de um objeto, permitindo que seja exibido de forma legível e informativa.
    