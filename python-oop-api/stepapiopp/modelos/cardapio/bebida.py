from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    # Conceito de Herança - A classe bebida herda os atributos nome e preco da classe ItemCardapio, além de adicionar um novo atributo tamanho.
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'{self._nome} - {self._tamanho} - R${self._preco:.2f}'
    ## O método __str__( é um método especial em Python que é chamado quando um objeto é convertido para uma string, como quando é impresso. Ele é usado para definir a representação em string de um objeto, permitindo que seja exibido de forma legível e informativa.
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
        ## O método aplicar_desconto é uma implementação concreta do método abstrato definido na classe ItemCardapio. Ele aplica um desconto de 5% ao preço da bebida, demonstrando o conceito de polimorfismo, onde a mesma interface (método aplicar_desconto) pode ter diferentes implementações em subclasses diferentes.
        ## O polimorfismo é um conceito fundamental na programação orientada a objetos que permite que objetos de diferentes classes sejam tratados como objetos da mesma classe base, desde que implementem os mesmos métodos ou interfaces. Isso promove a flexibilidade e a reutilização de código, permitindo que diferentes tipos de objetos sejam usados de maneira intercambiável.
        ## O método super() é usado para chamar um método da classe pai (superclasse) a partir de uma classe filha (subclasse). Ele é útil para acessar métodos ou atributos da classe pai que foram sobrescritos na classe filha, permitindo que a classe filha aproveite a funcionalidade da classe pai enquanto adiciona ou modifica comportamentos específicos.