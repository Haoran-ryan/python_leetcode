def bubble_sort(arr):
    # edge cases
    if arr is None or len(arr) < 2:
        return arr
    """
    Because buble sort confirms the largest element at the end of the array in each sort loop, we need to slice out the last element for the next loop.
    """
    for i in range(len(arr), 0, -1):
        for x in range(0,i-1): # i is the length of the array
            # if the current element is greater than the next element, swap them
            if arr[x] > arr[x+1]:
                print('\nbefore swap: ', arr)
                print("We are going to swap {} with {} at the index of {} and {}".format(arr[x], arr[x+1],x, x+1))
                arr[x], arr[x+1] = arr[x+1], arr[x]
                print('after swap: ', arr)
    print('Bubble sort completed: ', arr)
    
bubble_sort([7, 5, 3, 2, 4])