# Roteiro de estudo — Pipeline Python + API + POO

> Repo de curso, **três exercícios** de Python que juntos cobrem: ler/transformar
> dados de fontes diferentes, e modelar um domínio com Programação Orientada a
> Objetos (herança, classe abstrata, encapsulamento). Não tem servidor de
> verdade — "API" aqui é o desenho das classes que uma API usaria.
> Se você só tem 15 minutos: leia `pipelinedds/scripts/processamento_dados.py`.

## As três pastas

| Pasta | O que é | Conceito |
|---|---|---|
| `pipelinedds/` | ETL: lê um `.json` de uma "empresa A" e um `.csv` de uma "empresa B", junta, salva um `.csv` combinado | ler formatos diferentes com uma classe só; `csv.DictReader`, `json.load` |
| `poo-api/` | 1ª versão do modelo de restaurante: `Restaurante`, `Avaliacao` | classes simples, atributos, métodos |
| `python-oop-api/stepapiopp/` | versão evoluída: cardápio com hierarquia `ItemCardapio` → `Prato` / `Bebida` | **classe abstrata** (`ABC` + `@abstractmethod`), herança, polimorfismo |

Estude nessa ordem — cada uma adiciona uma ideia.

## Etapa 1 — `pipelinedds/` (dados)

**Leia:** `scripts/processamento_dados.py`.

A classe `Dados` recebe um `caminho` e um `tipo_dados` (`'csv'`, `'json'`, `'list'`)
e no `__init__` já lê o arquivo, descobre as colunas e conta as linhas. Repare que
o **construtor faz trabalho** (não só guarda os argumentos) — decisão comentada no
próprio código ("é como ligar a máquina").

**Depois:** `scripts/fusao_mercado_fev.py` usa a `Dados` pra juntar as duas fontes.

**Exercício:** adicione suporte a `tipo_dados == 'tsv'` (valores separados por tab).
✅ *pronto quando* `Dados("arquivo.tsv", "tsv")` lê certo e `get_columns()` funciona.

## Etapa 2 — `poo-api/` (POO básica)

**Leia:** `modelos/restaurante.py` e `modelos/avaliacao.py`.

Duas classes, atributos, um método que calcula a média das avaliações. É o
aquecimento pra Etapa 3.

## Etapa 3 — `python-oop-api/stepapiopp/` (POO com abstração)

**Leia, nesta ordem:**
1. `modelos/cardapio/item_cardapio.py` — a classe **base abstrata**. Define
   `aplicar_desconto` como `@abstractmethod` — um contrato que toda subclasse
   tem que cumprir.
2. `modelos/cardapio/prato.py` e `bebida.py` — as duas subclasses. Cada uma
   implementa `aplicar_desconto` à sua maneira (polimorfismo).
3. `modelos/restaurante.py` — usa `ItemCardapio` sem saber se é Prato ou Bebida.
4. `app.py` — o script que monta um restaurante e exibe o cardápio.

**Bug pra você achar (é exercício):**
- `item_cardapio.py` faz `class ItemCardapio():` — **sem herdar de `ABC`**. Com
  isso o `@abstractmethod` não é realmente forçado: dá pra instanciar
  `ItemCardapio()` direto, o que não devia. Conserte: `from abc import ABC,
  abstractmethod` e `class ItemCardapio(ABC):`. Teste que `ItemCardapio("x", 1)`
  passa a levantar `TypeError`.
- `app.py`, no `main()`: `restaurante_praca.exibir_cardapio` — falta o `()`, então
  não chama nada. (Já corrigido em 10/09, mas repare que estava lá — é o tipo de
  erro que só aparece quando você **roda** e não vê saída nenhuma.)

**Exercício final:** adicione uma terceira subclasse `Sobremesa` que herda de
`ItemCardapio`, com sua própria regra de desconto, e coloque uma no cardápio.
✅ *pronto quando* `python app.py` exibe as três (Prato, Bebida, Sobremesa).
