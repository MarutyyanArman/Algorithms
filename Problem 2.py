# Merge Sort Recursively

def MergeSortRecursive(arr):
    if len(arr) <= 1:
        return arr
    
    def combine(left, right):
        sorted_arr = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
        
        while i < len(left):
            sorted_arr.append(left[i])
            i += 1
        
        while j < len(right):
            sorted_arr.append(right[j])
            j += 1   

        return sorted_arr     

    mid_elm = len(arr) // 2
    left_part = MergeSortRecursive(arr[:mid_elm])
    right_part = MergeSortRecursive(arr[mid_elm:])

    return combine(left_part, right_part)

my_arr = [5, 1, 6, 2, 5, 1, 0, 3]
print(MergeSortRecursive(my_arr))