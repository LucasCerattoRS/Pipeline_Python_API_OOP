"""Testes mínimos do modelo de restaurante/cardápio.

Rodar (dentro de python-oop-api/stepapiopp): python -m unittest -v
"""

import contextlib
import io
import unittest

from modelos.cardapio.bebida import Bebida
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante


class TestCardapio(unittest.TestCase):
    def test_item_cardapio_e_abstrato(self):
        # Sem herdar de ABC, o @abstractmethod não vale e a base podia ser instanciada.
        with self.assertRaises(TypeError):
            ItemCardapio("genérico", 1.0)

    def test_descontos_polimorficos(self):
        bebida, prato = Bebida("suco", 10.0, "300ml"), Prato("bife", 100.0, "com arroz")
        bebida.aplicar_desconto()
        prato.aplicar_desconto()
        self.assertAlmostEqual(bebida._preco, 9.2)   # 8%
        self.assertAlmostEqual(prato._preco, 96.0)   # 4%

    def test_exibir_cardapio_e_metodo(self):
        # Com @property, `restaurante.exibir_cardapio()` dava TypeError: 'NoneType' object is not callable.
        r = Restaurante("praça", "gourmet")
        r.adicionar_no_cardapio(Bebida("suco", 5.0, "300ml"))
        r.adicionar_no_cardapio("não é item")  # ignorado pelo isinstance
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            r.exibir_cardapio()
        self.assertIn("1. Nome:suco", saida.getvalue())
        self.assertNotIn("2.", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
