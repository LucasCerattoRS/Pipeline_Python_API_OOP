class ItemCardapio:
    ## init é um método especial em Python que é chamado quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto.
    def __init__(self, nome: str, preco: float):
        ## Atributos privados
        self._nome = nome
        self._preco = preco

