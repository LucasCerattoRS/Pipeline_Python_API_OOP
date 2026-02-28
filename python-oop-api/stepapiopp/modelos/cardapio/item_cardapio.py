from abc import ABC, abstractmethod
class ItemCardapio():
    ## init é um método especial em Python que é chamado quando um objeto é criado a partir de uma classe. Ele é usado para inicializar os atributos do objeto.
    def __init__(self, nome: str, preco: float):
        ## Atributos privados
        self._nome = nome
        self._preco = preco

    @abstractmethod
    # O decorador @abstractmethod é usado para indicar que um método é abstrato, ou seja, que deve ser implementado por qualquer classe que herde da classe base. Ele é usado em conjunto com a classe ABC (Abstract Base Class) para criar classes abstratas em Python.
    ## O método aplicar_desconto é declarado como um método abstrato, o que significa que ele não tem uma implementação concreta na classe ItemCardapio. Qualquer classe que herde de ItemCardapio deve fornecer uma implementação para o método aplicar_desconto, garantindo que todas as subclasses tenham esse comportamento definido.

    def aplicar_desconto(self):
        pass
