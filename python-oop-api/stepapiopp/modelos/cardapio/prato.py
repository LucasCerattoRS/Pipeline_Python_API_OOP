from modelos.cardapio.item_cardapio import ItemCardapio
class prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        super().__init__(nome, preco)
        ## Super vai permitir que a classe prato herde os atributos nome e preco da classe ItemCardapio, evitando a necessidade de repetir o código para inicializar esses atributos.
        ## A vantagem de usar super() é que ele torna o código mais limpo e fácil de manter, além de permitir a reutilização de código em classes filhas.
        self._descricao = descricao