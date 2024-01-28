def findMax(arr,left,right):
    if left == right:
        return arr[left]
    mid = left + ((right - left) >> 2)
    leftMax = findMax(arr,left,mid)
    rightMax = findMax(arr,mid+1,right)
    return max(leftMax,rightMax)

# arr = [1,2,3,4,5,6,7,8,9,10]
arr = [3,5,7,4]
print(findMax(arr,0,len(arr)-1))