# -*- coding: utf-8 -*-
# @Author: qiaozhiqiang01
# @Date:   2018-03-13 18:26:18
# @Last Modified by:   NewCoderQ
# @Last Modified time: 2018-03-13 18:44:12

class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(32)])

if __name__ == '__main__':
    sol = Solution()

    sol.NumberOf1(-3)

