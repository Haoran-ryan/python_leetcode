# Week 1 

## Day 1 : 628 Maximum product of three numbers 

### My Reflection:
 Edge case:
    - a list of negative(2+) and positive ints
    - biggest product is 2 smallest negatives * the biggest positive 
 ### 网友 - 排序和不排序的解法
```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """排序方法，时间复杂度O(nlog(n))"""
        # nums.sort()
        # return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

        """遍历一遍数组，不使用排序，时间复杂度O(n)"""
        max1 = -float('inf')       # 第一大的值
        max2 = -float('inf')       # 第二大的值
        max3 = -float('inf')       # 第三大的值
        min1 = float('inf')        # 第一小的值
        min2 = float('inf')        # 第二小的值

        for num in nums:
            if num > max1:         # 啥？你比第一大的值还大？？那好吧，你去做老大
                max3 = max2        # 原老二委屈一下你，去做老三吧，难受...
                max2 = max1        # 原老大委屈一下你，去做老二吧，很难受...
                max1 = num         # 大哥快请上座！！！
            elif num > max2:       # 嗯？你比第二大的值大啊？？那行吧，老二给你做，别碰老大啊，他脾气不好...
                max3 = max2        # 原老二委屈一下你，去做老三吧，难受...
                max2 = num         # 二哥请上座！！
            elif num > max3:       # 别舞舞喳喳的，不就比第三大的值大么？？去去去，那个位置给你了...
                max3 = num         # 三哥上座！
            
            if num < min1:         # 啊？你比第一小的值还小，哈哈哈，笑死我了，来来来，快去！
                min2 = min1        # 原第一小，恭喜你，终于找到比你小的了，你现在是第二小！
                min1 = num         # 老实呆着，你现在是最小的了！！！
            elif num < min2:       # 哦？你比第二小的值小？比最小的还大，嗯..那你去做第二小
                min2 = num         # 来吧，你现在是第二小，原第二小解脱了！
            
        return max(max1 * max2 * max3, max1 * min1 * min2)

作者：我想找工作！
链接：https://leetcode.cn/problems/maximum-product-of-three-numbers/solutions/339839/pai-xu-fa-he-bu-pai-xu-de-fang-fa-du-zai-zhe-li-li/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

## Day 4 : 645 Set Mismatch 
我的做法非常地昂贵

### 官方题解
#### Hash
- 重复的数字在数组中出现 2次，丢失的数字在数组中出现 0 次，其余的每个数字在数组中出现 1 次。因此可以使用哈希表记录每个元素在数组中出现的次数，然后遍历从 111 到 nnn 的每个数字，分别找到出现 222 次和出现 000 次的数字，即为重复的数字和丢失的数字。
```javascript
var findErrorNums = function(nums) {
    const errorNums = new Array(2).fill(0);
    const n = nums.length;
    const map = new Map();
    for (const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
    }
    for (let i = 1; i <= n; i++) {
        const count = map.get(i) || 0;
        if (count === 2) {
            errorNums[0] = i;
        } else if (count === 0) {
            errorNums[1] = i;
        }
    }
    return errorNums;
};

作者：力扣官方题解
链接：https://leetcode.cn/problems/set-mismatch/solutions/857255/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
复杂度分析

- 时间复杂度：O(n)O(n)O(n)，其中 nnn 是数组 nums\textit{nums}nums 的长度。需要遍历数组并填入哈希表，然后遍历从 111 到 nnn 的每个数寻找错误的集合。

- 空间复杂度：O(n)O(n)O(n)，其中 nnn 是数组 nums\textit{nums}nums 的长度。需要创建大小为 O(n)O(n)O(n) 的哈希表。

#### Bit operation 位运算

使用位运算，可以达到 O(n) 的时间复杂度和 O(1)的空间复杂度。

重复的数字在数组中出现 2 次，丢失的数字在数组中出现 0 次，其余的每个数字在数组中出现 1 次。由此可见，重复的数字和丢失的数字的出现次数的奇偶性相同，且和其余的每个数字的出现次数的奇偶性不同。如果在数组的 n 个数字后面再添加从 1 到 n 的每个数字，得到 2n 个数字，则在 2n 个数字中，重复的数字出现 3 次，丢失的数字出现 1 次，其余的每个数字出现 2 次。根据出现次数的奇偶性，可以使用异或运算求解。

用 x 和 y 分别表示重复的数字和丢失的数字。考虑上述 2n 个数字的异或运算结果 xor，由于异或运算 ⊕ 满足交换律和结合律，且对任何数字 a 都满足 a⊕a=0 和 0⊕a=a，因此 xor=x⊕x⊕x⊕y=x⊕y，即 x 和 y的异或运算的结果。

由于 x≠y，因此 xor≠0令 lowbit=xor & (−xor)，则 lowbit为 x 和 y 的二进制表示中的最低不同位，可以用 lowbit 区分 x 和 y。

得到 llowbit 之后，可以将上述 2n 个数字分成两组，第一组的每个数字 a都满足 a & lowbit=0，第二组的每个数字 b 都满足 b & lowbit≠0。

创建两个变量 num1和 num2，初始值都为 0，然后再次遍历上述 2n 个数字，对于每个数字 a，如果 a & lowbit=0，则令 num1=num1⊕a，否则令 num2=num2⊕a。

遍历结束之后，num1为第一组的全部数字的异或结果，num2 为第二组的全部数字的异或结果。由于同一个数字只可能出现在其中的一组，且除了 x 和 y 以外，每个数字一定在其中的一组出现 2 次，因此 num1和 num2分别对应 x 和 y 中的一个数字，但是具体对应哪个数还未知。

为了知道 num1和 num2 分别对应 x 和 y 中的哪一个数字，只需要再次遍历数组 nums 即可。如果数组中存在元素等于 num1，则有 x=num1 和 y=num2，否则有 x=num2 和 y=num1。

作者：力扣官方题解
链接：https://leetcode.cn/problems/set-mismatch/solutions/857255/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```javascript
var findErrorNums = function(nums) {
    const n = nums.length;
    let xor = 0;
    for (const num of nums) {
        xor ^= num;
    }
    for (let i = 1; i <= n; i++) {
        xor ^= i;
    }
    const lowbit = xor & (-xor);
    let num1 = 0, num2 = 0;
    for (const num of nums) {
        if ((num & lowbit) === 0) {
            num1 ^= num;
        } else {
            num2 ^= num;
        }
    }
    for (let i = 1; i <= n; i++) {
        if ((i & lowbit) === 0) {
            num1 ^= i;
        } else {
            num2 ^= i;
        }
    }
    for (const num of nums) {
        if (num === num1) {
            return [num1, num2];
        }
    }
    return [num2, num1];
};

作者：力扣官方题解
链接：https://leetcode.cn/problems/set-mismatch/solutions/857255/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```