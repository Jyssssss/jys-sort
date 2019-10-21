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
