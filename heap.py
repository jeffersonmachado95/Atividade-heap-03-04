class MaxHeap:
    def __init__(self, array=None):
        self.heap = array if array else []
        if self.heap:
            self.build_max_heap()

    def max_heapify(self, i, n):
        """ Mantém a propriedade do heap de máximo """
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest, n)

    def build_max_heap(self):
        """ Constrói um heap de máximo a partir de um array desordenado """
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i, n)

    def heapsort(self):
        """ Ordena o array usando heapsort """
        self.build_max_heap()
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]  # Move o maior para o final
            self.max_heapify(0, i)
        return self.heap

# Exemplo de uso:
arr = [3, 19, 1, 14, 8, 7]
heap = MaxHeap(arr)
sorted_arr = heap.heapsort()
print("Array ordenado:", sorted_arr)
