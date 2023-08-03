'''
^ XOR operation can be understood as summation, where:
 1 + 0 = 1
 0 + 0 = 0
 1 + 1 = (1)0 , where one is not carried over
'''
a = '10110'
b = '00111'
# convert binary strings to integers
a_int = int(a, 2)
b_int = int(b, 2)

# bitwise XOR
result = a_int ^ b_int

print(bin(result)[2:])  # convert result back to binary string

"""交换结合律的应用
1. 减少空间使用
2. 前提： A, B 在内存空间中是各自独立的。如果不是，最后结果会是0。
"""
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

# -------------------------------
"""_例题_
1. 有一个正数数组 arr[int]
2. 其中有一个数出现了奇数次，其他数出现偶数次，请问这个奇数次的数是什么？
    - 用异或运算消消乐
3. 有两个数出现了奇数次，其他数均出现偶数次，请问这两个数是什么？
4. 要求时间复杂度是O(n)
"""

def printOddNum1(arr):
    eor = 0
    for element in arr:
        eor ^= element
    return eor 

print(printOddNum1([1,1,1,2,3,3,2]))