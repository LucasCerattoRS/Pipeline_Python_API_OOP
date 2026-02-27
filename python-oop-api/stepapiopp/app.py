from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de laranja', 5.0, '300ml')
prato_bife = Prato('bife acebolado', 20.0, 'bife acebolado com arroz e feijão')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_bife)

def main():
    pass
if __name__ == '__main__':
    main()