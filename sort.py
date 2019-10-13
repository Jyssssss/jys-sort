class Sort:
    def BubbleSort(self, collection):
        for i in range(len(collection), 0, -1):
            for j in range(i - 1):
                if collection[j] > collection[j + 1]:
                    temp = collection[j]
                    collection[j] = collection[j + 1]
                    collection[j + 1] = temp

    def InsertionSort(self, collection):
        for i in range(len(collection)):
            for j in range(i):
                if collection[i] < collection[j]:
                    temp = collection[j]
                    collection[j] = collection[i]
                    collection[i] = temp
