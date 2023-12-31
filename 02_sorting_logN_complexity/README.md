# Recursion 
1. 递归可以理解为"二叉树"
2. 例：
```python
arr = [3,2,5,6,7,4]
# -------------------
# 下标  0,1,2,3,4,5
```
3. 二叉树图例
```
               p(0,5)
            /           \
        p(0,2)           p(3,5)
        /    \          /      \
    p(0,1)   p(2,2)   p(3,4)    p(5,5)
    /    \             /    \
p(0,0) p(1,1)       p(3,3)   p(4,4)
```

## 中点选择
1. 不使用：mid = (left + right) // 2
2. 因为会有溢出的风险，所以使用：mid = left + (right - left) // 2
3. 简化：mid = left + (right - left) >> 1

# master 公式
1. T(N) = aT(N/b) + O(N^d)
2. 已知a,b,d，则时间复杂度为：
   1. 如果 log(b,a) > d, 则时间复杂度为：O(N^log(b,a))
   2. 如果 log(b,a) = d, 则时间复杂度为：O(N^d * logN)
   3. 如果 log(b,a) < d, 则时间复杂度为：O(N^d)
3. 补充阅读： www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html

# 归并排序 merge sort 
1. 简单递归：左边排好序、右边排好序、让其整体有序
2. 整体有序的过程：排外序方法
3. 时间复杂度：O(N*logN)
4. 空间复杂度：O(N)

```
result = [1,2,2,3,5,6]
arr = [3,2,1,5,6,2]
------------|------------
      1,2,3  2,5,6
      x      x      左边<右边，左边拷贝入结果数组
         x   x      左边=右边，默认拷贝左边入结果数组
           x x      左边>右边，右边拷贝入结果数组
           x   x    左边<右边，左边拷贝入结果数组
            x       左边超出边界，右边剩余结果拷贝入结果数组
```
