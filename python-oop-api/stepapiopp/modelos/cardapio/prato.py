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

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.04)
        ## O método aplicar_desconto é uma implementação concreta do método abstrato definido na classe ItemCardapio. Ele aplica um desconto de 10% ao preço do prato, demonstrando o conceito de polimorfismo, onde a mesma interface (método aplicar_desconto) pode ter diferentes implementações em subclasses diferentes.
        ## O polimorfismo é um conceito fundamental na programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos da mesma classe base, desde que implementem os mesmos métodos ou interfaces. Isso promove a flexibilidade e a reutilização de código, permitindo que diferentes tipos de objetos sejam usados de maneira intercambiável.
        ## O método super() é usado para chamar um método da classe pai (superclasse) a partir de uma classe filha (subclasse). Ele é útil para acessar métodos ou atributos da classe pai que foram sobrescritos na classe filha, permitindo que a classe filha aproveite a funcionalidade da classe pai enquanto adiciona ou modifica comportamentos específicos.
        ## obriga a ter o metodo mas nao para aplicar o desconto, ou seja, cada classe filha pode implementar o método aplicar_desconto de maneira diferente, aplicando descontos específicos para cada tipo de item do cardápio, como pratos e bebidas. Isso é um exemplo clássico de polimorfismo, onde a mesma interface (método aplicar_desconto) pode ter diferentes implementações em subclasses diferentes.