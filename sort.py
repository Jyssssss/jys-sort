class Sort:
    def _swap(self, collection, i, j):
        collection[i], collection[j] = collection[j], collection[i]

    def bubble_sort(self, collection):
        for i in range(len(collection), 0, -1):
            for j in range(i - 1):
                if collection[j] > collection[j + 1]:
                    self._swap(collection, j, j + 1)

    def insertion_sort(self, collection):
        for i in range(len(collection)):
            for j in range(i):
                if collection[i] < collection[j]:
                    self._swap(collection, i, j)

    def selection_sort(self, collection):
        for i in range(len(collection)):
            for j in range(i, len(collection)):
                if collection[j] < collection[i]:
                    self._swap(collection, i, j)

    def heap_sort(self, collection):
        def _create_heap(index, length):
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            is_heap = ((left_index >= length or collection[index] >= collection[left_index]) and
                       (right_index >= length or collection[index] >= collection[right_index]))
            if not is_heap:
                swap_index = None
                if left_index >= length:
                    swap_index = right_index
                elif right_index >= length:
                    swap_index = left_index
                elif collection[left_index] > collection[right_index]:
                    swap_index = left_index
                else:
                    swap_index = right_index
                self._swap(collection, index, swap_index)
                _create_heap(swap_index, length)

        # Heapify
        for i in reversed(range(len(collection))):
            _create_heap(i, len(collection))

        # Remove elements from top of the heap and place to the end.
        for i in reversed(range(len(collection))):
            self._swap(collection, 0, i)
            _create_heap(0, i)

    def quick_sort(self, collection):
        def _partition(start, end):
            pivot = collection[end]
            j = start
            for i in range(start, end):
                if collection[i] < pivot:
                    self._swap(collection, i, j)
                    j += 1
            self._swap(collection, end, j)
            return j

        def _quick_sort(start, end):
            if start < end:
                mid = _partition(start, end)
                _quick_sort(start, mid - 1)
                _quick_sort(mid + 1, end)

        _quick_sort(0, len(collection) - 1)

    def merge_sort(self, collection):
        def _merge_sort(subcollection):
            if len(subcollection) == 1:
                return subcollection
            else:
                left = _merge_sort(subcollection[:len(subcollection) // 2])
                right = _merge_sort(subcollection[len(subcollection) // 2:])
                l, r, i = 0, 0, 0
                while l < len(left) or r < len(right):
                    if r == len(right) or (l < len(left) and left[l] < right[r]):
                        subcollection[i] = left[l]
                        l += 1
                    else:
                        subcollection[i] = right[r]
                        r += 1
                    i += 1
                return subcollection

        _merge_sort(collection)
