from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('suco de laranja', 5.0, '300ml')
bebida_suco.aplicar_desconto()
prato_bife = Prato('bife acebolado', 20.0, 'bife acebolado com arroz e feijão')
prato_bife.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_bife)

def main():
    restaurante_praca.exibir_cardapio
if __name__ == '__main__':
    main()