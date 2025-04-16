# MaxHeap - Implementação de Heap de Máximo e Heapsort em Python

Este repositório contém a implementação de uma estrutura de dados `MaxHeap`, que é uma árvore binária onde o valor de cada nó é maior ou igual aos valores de seus filhos. Além disso, a classe oferece uma implementação do algoritmo **Heapsort**, que é baseado na estrutura `MaxHeap` para ordenar um array.

## Estrutura da Classe

### `MaxHeap`
A classe `MaxHeap` implementa um heap de máximo com os seguintes métodos:

#### Métodos

- **`__init__(self, array=None)`**:
  - Construtor que inicializa o heap a partir de um array fornecido ou cria um heap vazio.
  - Se um array for fornecido, o método `build_max_heap()` é chamado para garantir que a propriedade de máximo seja mantida.

- **`max_heapify(self, i, n)`**:
  - Método recursivo para manter a propriedade do heap de máximo.
  - Garantirá que o sub-árvore com a raiz em `i` tenha o maior valor em relação a seus filhos, ajustando o heap conforme necessário.

- **`build_max_heap(self)`**:
  - Constrói um heap de máximo a partir de um array desordenado.
  - Chama o método `max_heapify` para cada nó do meio até a raiz.

- **`heapsort(self)`**:
  - Ordena o array usando o algoritmo **Heapsort**.
  - Utiliza o `build_max_heap` para inicializar o heap e, em seguida, reorganiza os elementos, movendo o maior valor para o final e ajustando o heap iterativamente.

## Exemplo de Uso

```python
arr = [3, 19, 1, 14, 8, 7]
heap = MaxHeap(arr)
sorted_arr = heap.heapsort()
print("Array ordenado:", sorted_arr)
