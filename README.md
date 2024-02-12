# 01. 认识时间复杂度、简单排序

### 什么是时间复杂度？

- **to measure the performance of constant operations** 

#### 常数操作

1. Arithmetic operations: +, -, *, /, %, //, **
2. Bitwise operations: &, |, ^, ~, <<, >>
3. Boolean operations: and, or, not
4. Comparison operations: <, <=, >, >=, ==, !=
5. Identity operations: is, is not
6. Membership operations: in, not in
7. etc.
8. 与数据量无关的操作

#### 非常数操作

e.g. 
1. fetch [i] in a linked list 

## 等差数列 （求前n项和）

- 已知首选、末项、项数，求和 （倒序相加法）
$S_n = \frac{n \times (a_1 + a_2)}{2}$ 
- 已知首项、项数、公差，求和
$S_n = a_1 \times n + \frac{n \times (n-1)}{2} \times d$

## 选择排序

- 基本思想：在每次迭代中找到剩余未排序部分的最小元素,并将其放到正确的位置。
- 步骤
  - works by repeatedly finding the smallest element in an array and swapping it with the first element in the array.
  2. starts at the beginning of the array and compares the first element with the remaining elements in the array. The smallest element is found and swapped with the first element.
  3. then moves on to the next element and repeats the process. This continues until the end of the array is reached.

### 代码1

```python
# 错误版本：
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

#### 代码1的错误

1. 不应该在循环中交换值；应该做的是更新min_index的位置
2. j指针应该应该始终和min_index有关，即是min_i_dex的后一位（最小值的下一位），所以不能初始1后再 +=1

### 代码2

```python
# 正确的写法
def selectionSort(arr):
    for i in range(len(arr) - 1):
        #记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
```

1. 排序子数组的范围 ： 0 ~ len - 1
2. 因为最后一个子数组一定是最大的，不需要排序（前面已经排完了）
3. 子循环中 j 是锁定 minIndex
4. python中需要再循环外调换元素值

## 冒泡排序

1. 从index-0开始，对比0,1上的元素大小，如1<0则交换
2. 依次类推，对比1,2; 2,3 ...
3. 第一次循环结束，就可以确定**最后一个元素**在正确的位置上
4. 以此类推，确定倒数2，3 ...

### 时间复杂度

$O(N^2)$

### 代码

```python
def bubble_sort(arr):
    # edge cases
    if arr is None or len(arr) < 2:
        return arr
    """
    Because buble sort confirms the largest element at the end of the array in each sort loop, we need to slice out the last element for the next loop.
    """
    for i in range(len(arr), 0, -1):
        for x in range(0,i-1): # i is the length of the sliced array
            # if the current element is greater than the next element, swap them
            if arr[x] > arr[x+1]:
                print('\nbefore swap: ', arr)
                print("We are going to swap {} with {} at the index of {} and {}".format(arr[x], arr[x+1],x, x+1))
                arr[x], arr[x+1] = arr[x+1], arr[x]
                print('after swap: ', arr)
    print('\n😁 Bubble sort completed: ', arr)
    
bubble_sort([7, 5, 3, 2, 4])
```

## 异或运算

1. 可以理解为*无进位相加*
2. 性质：
    1. 任何数N和0异或，结果为N
    2. 任何数N和自己异或，结果为0
    3. 交换律：确实，异或操作遵循交换律，即 a⊕b=b⊕aa⊕b=b⊕a。
    4. 结合律：异或操作也遵循结合律，即 a⊕(b⊕c)=(a⊕b)⊕ca⊕(b⊕c)=(a⊕b)⊕c。
    5. 分配律：异或操作不遵循分配律。在布尔代数中，分配律通常指的是与（AND）和或（OR）操作。异或操作的分配律形式 a⊕(b⊕c)=(a⊕b)⊕(a⊕c)a⊕(b⊕c)=(a⊕b)⊕(a⊕c) 并不成立。

### 2个以上数字的异或运算

- 先后顺序不会有任何影响

### 例1 - 交换a, b两数的值

1. a = a^b
2. b = a^b 由于在(1)中，a有重新赋值，因此 $b_2$= a^b^b = a
3. a = a^b 同理，由于(1)(2)中对a,b都有重新赋值，因此 $a_3$ = a^b^a = b

- *注意: a,b必须指向内存中的不同地址* 
- 例如，在数组中调换arr[i] arr[j]的值，必须确保i!=j。否则XOR调换后，最后这位置上的数会为0

#### 代码

```python
a = '10110'
b = '00111'
# convert binary strings to integers
a_int = int(a, 2)
b_int = int(b, 2)

# bitwise XOR
result = a_int ^ b_int

print(bin(result)[2:])  # convert result back to binary string

# 10001
```

### 例2 - 交换律、 结合律

1. 减少空间使用
2. 前提： A, B 在内存空间中是各自独立的。如果不是，最后结果会是0。

#### 代码

```python
# commtativity & associativity 
# 假设 A = 甲， B = 乙
A = 17
B = 23
A = A^B # 新A = 甲 ^ 乙
print(A)
B = A^B # 新B = 甲 ^ 乙 ^ 乙 ； 根据交换结合律 , 得 甲^(乙^乙) = 甲
print(B)
A = A^B  # 新A = 甲 ^ 乙 ^ 甲 = 乙
print(A)
```

### 例3 - 寻找唯一不成对的数

1. 有一个正数数组 arr[int]
2. 其中有一个数出现了奇数次，其他数出现偶数次，请问这个奇数次的数是什么？
    - 用异或运算消消乐
3. 有两个数出现了奇数次，其他数均出现偶数次，请问这两个数是什么？
4. 要求时间复杂度是O(n)

#### 代码

```python
def printOddNum1(arr):
    eor = 0
    for element in arr:
        eor ^= element
    return eor 

print(printOddNum1([1,1,1,2,3,3,2]))
```

### 例4 - 寻找唯二不成对的数

- 有两个数出现了奇数次，其他数均出现偶数次，请问这两个数是什么？
1. 重复[2]的步骤，获得EOR = a ^ b （两个奇数的异或结果） 
2. 已知a !=b (如果相等，那么eor = 0)，因此EOR这个结果中，至少有一位是1。假设1是在k位置上。
3. 再次遍历所有的数字，并只对所有k位置上是1的数字进行异或运算（也可选择对K位置上是0的数字进行异或运算），将结果赋值给 EOR'。
4. 异或计算 EOR ^ EOR'  = a ^ b ^ a = b。获得2个奇数中的一个，假设是b
5. 将这个数值 b ^ EOR = a。获得另一个的奇数

#### 将二进制数的最右边的1取出来

```python
def get_rightest_one(n):
    return n & (~n + 1)
```
```
e.g: 
 EOR =              10101000
~EOR =              01010111
~EOR + 1 =          01011000
----------------------------
                        x     // 最右边的1

EOR & (~EOR + 1) =  00001000  // &按位与，只有1&1=1，其他都是0
```

`~` 取反运算
- 在二进制中,将每个位上的1变为0,0变为1 

`&` 与运算
- 1 & 1 = 1 ； 其他数字相与都是0

关于“补码”
- 任何整数`n` 的补码都是 `~n+1`
- 这是因为 `n+(~n+1) = n-n+1-1 = 0`

#### 代码

```python
def printOddNum2(arr):
    EOR = 0
    for x in range(len(arr)):
        EOR ^= arr[x]
    print('两个奇数的异或结果: {}, 用二进制表达就是{} '.format(EOR, bin(EOR)[2:]))
    
    farRightOne = EOR & (~EOR + 1)
    
    onlyOne = 0 #即eor'
    for x in range(len(arr)):
        # 通过与运算，找到在k位置上为1的所有数；并进行异或运算
        if (arr[x] & farRightOne == 0):  # ==0 的如果是a , 那么 ==1 的就是b
            onlyOne ^= arr[x]
    print('其中的一个奇数 :', onlyOne)
    print('则另一个奇数是 :', EOR ^ onlyOne)
    
printOddNum2([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10]) # 9,10
```

## 插入排序

复杂度分析

- Time Complexity: O(n^2)
- Space Complexity: O(1)

### 伪代码

```python
     [3 ,2, 5, 4, 2, 3, 3]  
     ----------------------
      0  1  2  3  4  5  6
- 1st iteration [0] 
- 2nd iteration [0, 1] : arr[0] > arr[1] => swap => [2,3,5,4,2,3,3] 0~1有序
- 3rd iteration [0, 1, 2] : arr[1] < arr[2] => no swap => [2,3,4,5,2,3,3] 0~2有序
- 4th iteration [0, 1, 2, 3] : arr[2] < arr[3] => no swap => [2,3,4,5,2,3,3] 0~3有序
- 5th iteration [0, 1, 2, 3, 4] : 
                                arr[3] > arr[4] => swap => [2,3,4,2,5,3,3] 0~4有序? False 
                                arr[2] > arr[3] => swap => [2,3,2,4,5,3,3] ...
                                arr[1] > arr[2] => swap => [2,2,3,4,5,3,3] 0~4有序

以此类推
```

### 代码

```python
def insertion_sort(arr):
    # edge cases 
    if arr is None or len(arr)<2:
        return arr 
    
    for i in range(1, len(arr)): # 每一步的目标，0 ~ i上有序
        print("\n现在处理的是数组中的下位从0 ~ {}的部分，即{}".format(i,arr[:i+1]))
        
        for j in range(i-1, -1, -1): # 从i-1开始，往前看，如果i-1和i不满足顺序，就交换 
    
            # 要么i-1开始，对比 j ,j +1 ；那么i开始，对比j-1, j
            print("对比的是{}和{}位置上的数".format(j, j+1))
            
            if j>=0 and arr[j]>arr[j+1]:
                print("发现{}和{}位置上的数不满足顺序，交换".format(j, j+1))
                print("交换前的数组是{}".format(arr))
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("交换后的数组是{}".format(arr))
            else:
                print("发现{}和{}位置上的数满足顺序，不交换".format(j, j+1))
    return arr 
```

## 二分查找

### 用例

1. 有序数组中，找某个数是否存在 $O(log_{2}N)$
2. 有序数组中，找到>=某个数最左侧的位置 
3. 局部最小值问题，这时候可以是无序数组

### 代码

```python
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right: # =条件包括在内，确保数组只包含一个元素时，这个算法也能成功
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:  # arr[mid] < target
            left = mid + 1
    
    return False  # 如果循环结束仍未找到，则返回False

```

```python
a = [1,2,3,4,5,6,7,9,10]
b = 5
c = 8

print(binarySearch(a,b))
print(binarySearch(a,c))
```

### 例1 

用二分法查找包含重复数字的、有序数组中，大于等于目标数组最左位置的对应数字的下标， 如

- 数组 [1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,5,5,5,5,5] 
- 找到 Target = 3 在以上数组中最左侧3的下标
- 与普通二分法的区别是，这个查找必须要找到最后一个元素
- 类似，也可以用来寻找小于等于目标最右侧的数字下标

#### 代码

```python
def far_left_position(arr, target):
    left = 0
    right = len(arr) - 1
    t = -1  # 如果找不到，返回-1表示不存在

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            t = mid # t= min(mid,t) 这是安全且逻辑正确，但是没有必要的
            right = mid - 1  # 继续向左搜索
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if t == -1:
        print("The target number {} is not found in the array".format(target))
    else:
        print("The target number {} is located at index {} in the array".format(target, t))

```

### 用二分法解局部最小

题目
1. 在无序数组中，相邻的数字一定不相等，找到该数组中任一一个局部最小数字的下标，复杂度优于O(N)
2. 局部最小的定义：
    1. 如果 arr[0] < arr[1] , arr[0]就是局部最小
    2. 如果 arr[n-1] < arr[n-2], arr[n]就是局部最小
    3. 如果 arr[n-k] < arr[n-k+1] 且 arr[n-k] < arr[n-k-1]， 那么arr[n-k]就是局部最小
3. 无序数组一定存在“局部最小”

## 对数器

- 有：方法A(想测试的方法）；方法B(是不计较优化的好实现的方法）
- 随机方法产生器：通过A获得结果a ; B -> b 
- a ?= b

## `Math.random()` 

概率返回随机整数

- random() => [0,1)所有小数，等概率返回一个
- random() * N => [0, N) 所有小数，等概率返回一个
- int(random() * N) => [0, N-1] 所有整数，等概率返回一个

# 02. 递归

## 二进制右移1位 = 原数除以2

>  - mid = left + (right - left) // 2 
> - 简化为 mid = L + (R-L) >> 1 *

在二进制表示中，每个数字的位置代表一个特定的值，这个值是2的幂。从右向左看，最右边的位代表 `2^0`（即1），下一位代表 `2^1`（即2），再下一位代表 `2^2`（即4），以此类推。

例如，二进制数 1011 表示为：

    1×23=81×23=8
    0×22=00×22=0
    1×21=21×21=2
    1×20=11×20=1

所以 1011 等于 8+0+2+1=118+0+2+1=11。
右移操作

右移一位操作，意味着将二进制数中的每一位都向右移动一个位置。这会导致最右边的一位被丢弃，而最左边会根据具体的右移类型（逻辑右移或算术右移）添加一位（通常是0）。在数值层面，这个操作相当于将每个位代表的值都减少一半（因为 2n2n 变成 2n−12n−1）。
例子

举个例子，假设我们有一个二进制数 1100（十进制中的12）：

    二进制 1100 表示为：
        1×23=81×23=8
        1×22=41×22=4
        0×21=00×21=0
        0×20=00×20=0
        总和 = 12
    
    如果我们对 1100 进行右移一位操作，得到 0110：
        0×23=00×23=0
        1×22=41×22=4
        1×21=21×21=2
        0×20=00×20=0
        总和 = 6

通过这个操作，原来的值12变成了6，正好是原值的一半。这就是为什么在二进制表示中，右移一位等同于除以2。

`2^n / 2 = 2^(n-1)`



## 求数组中的最大值

### Ver 1 

```python
def find_max(arr):
    # Base case: If the array has only one element, return that element
    if len(arr) == 1:
        return arr[0]

    # Recursive case: Find the maximum in the rest of the array
    max_of_rest = find_max(arr[1:])

    # Return the maximum of the first element and the maximum of the rest
    return max(arr[0], max_of_rest)

```

Consider an array [3, 1, 4, 2]. Here's how the process works:

- We want to find the max of [3, 1, 4, 2]. We compare 3 with the max of [1, 4, 2].
- To find the max of [1, 4, 2], we compare 1 with the max of [4, 2].
- To find the max of [4, 2], we compare 4 with the max of [2].
- The max of [2] is 2 (base case), so now we start comparing back up:
  - max(4, 2) = 4, so the max of [4, 2] is 4.
  - Then, max(1, 4) = 4, so the max of [1, 4, 2] is 4.
  - Finally, max(3, 4) = 4, so the max of [3, 1, 4, 2] is 4.

### Ver 2

```python
def find_max2(arr, l, r): # 这个符合master公式
    if l == r:
        return arr[l]
    
    mid = l + ((r-l)>>1)
    lMax = find_max2(arr, l, mid)
    rMax = find_max2(arr, mid+1, r)
    return max(lMax, rMax)
```

## Master 公式

- T(N) = a * T (N/b) + O(N^d)
    - T(N) 母问题的数据量是 N 级别
    - T (N/b) 所有子问题的规模都是 N/b 级别 （子问题规模是等量的）
    - a 子问题调用次数
    - O(N^d) 除去子问题调用之外，剩下过程的时间复杂度

### Master公式：求递归时间复杂度
- `find_max2`递归函数符合Master: a = 2, b =2 , d = 0
- n 是递归时候**当前的规模**，不需要在乎每一次递归时候实际n的变化

## 归并排序

**概念**：
归并排序是一种高效的排序算法，采用分治法（Divide and Conquer）策略。它通过递归地将列表分成两半，对每半进行排序，然后将排序好的两半合并在一起。

**核心步骤**：

1. **分解**：将待排序数组分解成两个子数组的过程。
2. **合并**：将两个排序好的子数组合并成一个最终的排序数组。

**合并操作**：
- 使用双指针技术比较两个数组的元素，将较小的元素先添加到结果数组中。
- 当其中一个数组的元素全部被选取后，将另一个数组的剩余元素直接追加到结果数组中。

**递归逻辑**：
- 递归地对数组进行分半处理，直到数组长度小于或等于1（这是基准情况，不需要进一步排序）。
- 然后递归地对这些分半后的数组进行排序和合并。

**重要概念**：
- **基准情况**：递归函数的停止条件，对于归并排序来说，是当处理的数组长度小于或等于1。
- **分而治之**：将大问题分解成小问题解决，然后将小问题的解决方案合并起来解决大问题。

**代码实现**：

```python
def merge(left, right):
    result = []  # 最终的排序结果列表
    i, j = 0, 0  # 初始化两个列表的指针

    # 当两个列表都有元素时
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将剩余元素追加到结果列表中
    result += left[i:]
    result += right[j:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 基准情况，直接返回列表

    mid = len(arr) // 2  # 找到中间索引
    left = merge_sort(arr[:mid])  # 对左半部分递归排序
    right = merge_sort(arr[mid:])  # 对右半部分递归排序

    return merge(left, right)  # 合并两个排序好的子列表

```

**递归过程示例**：
以数组 `[38, 27, 43, 3]` 为例，归并排序的过程可以表示为：

```
          [38, 27, 43, 3]
             /       \
       [38, 27]     [43, 3]
        /   \         /   \
     [38]  [27]     [43]  [3]
        \   /         \   /
       [27, 38]     [3, 43]
             \       /
          [3, 27, 38, 43]
```

**理解递归**：
在最顶层，每个子数组只有单一元素时，合并操作主要发生在比较这些单一元素并将它们按顺序合并的过程中。这确保了每一步合并都是在构建排序好的子数组，直到最后所有子数组合并成一个完整的排序数组。

### 代码

```python
def merge(left, right):
    result = []  # 最终的排序结果列表
    i, j = 0, 0  # 初始化两个列表的指针

    # 当两个列表都有元素时
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将剩余元素追加到结果列表中
    result += left[i:]
    result += right[j:]

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 基准情况，直接返回列表

    mid = len(arr) // 2  # 找到中间索引
    left = merge_sort(arr[:mid])  # 对左半部分递归排序
    right = merge_sort(arr[mid:])  # 对右半部分递归排序

    return merge(left, right)  # 合并两个排序好的子列表

```

### 归并排序扩展

#### 小和问题
- 在一个数组中，每一个左边比当前数小的数累加起来
- 如：[1,3,4,2,5] 1左边不存在>1的数字；3左边>3的数字有：1；4左边有：1,3;2左边有：1；5左边有：1,3,4,2
- 所以小和等于 `1+1+3+1+1+3+4+2 = 16`
