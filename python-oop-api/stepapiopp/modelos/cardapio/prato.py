from modelos.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        ## Super vai permitir que a classe prato herde os atributos nome e preco da classe ItemCardapio, evitando a necessidade de repetir o código para inicializar esses atributos.
        ## A vantagem de usar super() é que ele torna o código mais limpo e fácil de manter, além de permitir a reutilização de código em classes filhas.
        self._descricao = descricao

    def __str__(self):
        return f'{self._nome} - {self._descricao} - R${self._preco:.2f}'
    ## O método __str__ é um método especial em Python que é chamado quando um objeto é convertido para uma string, como quando é impresso. Ele é usado para definir a representação em string de um objeto, permitindo que seja exibido de forma legível e informativa.