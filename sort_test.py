import sort

jysSort = sort.Sort()
collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.bubble_sort(collection)
print('Bubble Sort:   ', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.insertion_sort(collection)
print('Insertion Sort:', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.selection_sort(collection)
print('Selection Sort:', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.heap_sort(collection)
print('Heap Sort:     ', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.quick_sort(collection)
print('Quick Sort:    ', collection)

collection = [9, 2, 5, 7, 1, 3, 4, 8, 6, 10]
jysSort.merge_sort(collection)
print('Merge Sort:    ', collection)
