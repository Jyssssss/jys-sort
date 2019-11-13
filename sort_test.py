import sort

jysSort = sort.Sort()
collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.BubbleSort(collection)
print('Bubble Sort:   ', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.InsertionSort(collection)
print('Insertion Sort:', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.SelectionSort(collection)
print('Selection Sort:', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.HeapSort(collection)
print('Heap Sort:     ', collection)
