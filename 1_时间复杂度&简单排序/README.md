# 时间复杂度
- 用来测量常数操作的指标

## `常数操作`？ 
- `+ - * /`, bitwise operation 都是常数操作
- 和数据量无关的操作

```c
int a = arr[i]
```

- 什么是"非常数操作"？
如，获得链表中的i 
```c
int b = list.get(i) 
```

## `时间复杂度`？ 
- 若两个流程 O(N)相同，那么要比较常数
- 如果常数也相同，那么只能实际测试两个流程的表现

# 等差数列前N项和
- 已知首选、末项、项数，求和 （倒序相加法）
$S_n = \frac{n \times (a_1 + a_2)}{2}$ 
- 已知首项、项数、公差，求和
$S_n = a_1 \times n + \frac{n \times (n-1)}{2} \times d$

# 选择排序
## 找茬 - 我的错误解法
```python
def selection_sort(arr):
    # rule out edge cases 
    if arr is None or len(arr) < 2:
        return arr
    # loop through the arr 
    i = 0
    j = 1
    while i < len(arr):
        # assume the min value is the first element
        min_index = i
        while j < len(arr):
            # any value less than the min value, update the min value
            if(arr[j] < arr[min_index]):
                # found new min value, update the min value
                min_index = j
                # swap the values 
                print('before swap: ', arr)
                arr[i], arr[j] = arr[j], arr[i]
                print('after swap:', arr)
            j += 1
        i += 1
    print(arr)

selection_sort([1, 3, 2, 5, 4])
```
1. 不应该在循环中交换值
2. j指针应该是i的后一位（最小值的下一位），所以不能初始1，后做 +=1

# 冒泡排序