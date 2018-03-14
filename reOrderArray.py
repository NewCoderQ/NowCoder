# -*- coding: utf-8 -*-
# @Author: NewCoderQ
# @Date:   2018-03-13 18:46:45
# @Last Modified by:   NewCoderQ
# @Last Modified time: 2018-03-14 13:53:17

"""
    重新排序一个整型数组
    要求：
        奇数在数组的左半边，偶数在数组的右边
        并且奇数和奇数、偶数和偶数之间的相对位置不变

    解决思路：
    1、创建一个指针 i 从左边第一个元素查找偶数
    2、接着第二个指针 j 从 i++ 的位置开始查找奇数
    3、将找到的奇数填充到数组中 i 的位置，i++ - j 位置的元素往后移动一个位置
    4、接着从 j++ 的位置往右查找奇数，再次进行调换

"""

class Solution:
    def reOrderArray(self, array):
        # 创建一个索引 i, 从数组的左侧开始查找偶数
        i = j = 0        # 初始化为0，从数组的第一个元素开始
        if len(array) == 0 or len(array) == 1:
            return array
        while i < len(array):
            index = 1
            if array[i] % 2 == 0:    # 指定位置的元素为偶数
                # 此处应该创建 while 循环
                j = i
                while j < len(array) - 1:
                    # 从后一个元素开始查找第一个出现的奇数
                    for j in range(j + 1, len(array)):
                        if array[j] % 2 == 1:        # 奇数
                            break
                        elif j == len(array) - 1:
                            print(array)
                            return array
                    tmp = array[j]                    # 奇数，暂存
                    for k in range(j - 1, i - 1, -1):
                        array[k + 1] = array[k]
                    array[i] = tmp
                    print(index, i, j, array)
                    index += 1
                    i += 1
                break

            else:                    # 指定位置的元素为奇数
                i += 1

if __name__ == '__main__':
    sol = Solution()
    sol.reOrderArray([1,3,5,7,2,4,6])
