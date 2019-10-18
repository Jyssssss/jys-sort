import sort

mySort = sort.Sort()
arr = [9, 0, 2, 5, 7, 1, 3, 4, 8, 6, 10]
mySort.BubbleSort(arr)
print('Bubble Sort:   ', arr)

arr = [9, 0, 2, 5, 7, 1, 3, 4, 8, 6, 10]
mySort.InsertionSort(arr)
print('Insertion Sort:', arr)

arr = [9, 0, 2, 5, 7, 1, 3, 4, 8, 6, 10]
mySort.SelectionSort(arr)
print('Insertion Sort:', arr)
