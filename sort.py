class Sort:
    def _swap(self, collection, i, j):
        temp = collection[i]
        collection[i] = collection[j]
        collection[j] = temp

    def BubbleSort(self, collection):
        for i in range(len(collection), 0, -1):
            for j in range(i - 1):
                if collection[j] > collection[j + 1]:
                    self._swap(collection, j, j + 1)

    def InsertionSort(self, collection):
        for i in range(len(collection)):
            for j in range(i):
                if collection[i] < collection[j]:
                    self._swap(collection, i, j)

    def SelectionSort(self, collection):
        for i in range(len(collection)):
            for j in range(i, len(collection)):
                if collection[j] < collection[i]:
                    self._swap(collection, i, j)

    def HeapSort(self, collection):
        def _createHeap(index, length):
            leftIndex = 2 * index + 1
            rightIndex = 2 * index + 2
            isHeap = ((leftIndex >= length or collection[index] >= collection[leftIndex]) and
                      (rightIndex >= length or collection[index] >= collection[rightIndex]))
            if not isHeap:
                swapIndex = None
                if leftIndex >= length:
                    swapIndex = rightIndex
                elif rightIndex >= length:
                    swapIndex = leftIndex
                elif collection[leftIndex] > collection[rightIndex]:
                    swapIndex = leftIndex
                else:
                    swapIndex = rightIndex
                self._swap(collection, index, swapIndex)
                _createHeap(swapIndex, length)

        # Heapify
        for i in reversed(range(len(collection))):
            _createHeap(i, len(collection))

        # Remove elements from top of the heap and place to the end.
        for i in reversed(range(len(collection))):
            self._swap(collection, 0, i)
            _createHeap(0, i)

    def QuickSort(self, collection):
        def _partition(start, end):
            pivot = collection[end]
            j = start
            for i in range(start, end):
                if collection[i] < pivot:
                    self._swap(collection, i, j)
                    j += 1
            self._swap(collection, end, j)
            return j

        def _quicksort(start, end):
            if start < end:
                mid = _partition(start, end)
                _quicksort(start, mid - 1)
                _quicksort(mid + 1, end)

        _quicksort(0, len(collection) - 1)
