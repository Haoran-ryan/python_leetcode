def selection_sort(arr):
    # rule out edge cases 
    if arr is None or len(arr) < 2:
        return arr
    # loop through the arr 
    i = 0
    while i < len(arr):
        # assume the min value is the first element
        min_index = i
        j = i + 1  # reset j at the beginning of each outer loop
        # compare the assumed min value at min_index with the value next to it
        while j < len(arr):
            # any value less than the min value, update the min value
            if arr[j] < arr[min_index]:
                # any value less than the min value, update the min value
                min_index = j
            j += 1
        # swap the new min value
        print('before swap: ', arr)
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print('after swap: ', arr)
        i += 1

    print('selection sort result: ', arr)

selection_sort([1, 3, 2, 5, 4])