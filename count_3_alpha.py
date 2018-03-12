# -*- coding: utf-8 -*-
# @Author: qiaozhiqiang01
# @Date:   2018-03-12 17:37:39
# @Last Modified by:   qiaozhiqiang01
# @Last Modified time: 2018-03-12 17:40:57

# 统计首先出现三次的英文字符
from __future__ import print_function

src_row = raw_input()            # 获取输入

# 创建字典来标记某个字母出现的次数
alpha_count = dict()
# 判断某个字符是否是字母
for item in src_row:            # 遍历字符串中的每一个字符
    if item.isalpha():
        # 是字符
        # 判断是否在 alpha_count 字典中出现过
        if item in alpha_count:
            # 出现过
            alpha_count[item] += 1
            if alpha_count[item] == 3:
                print(item)
                break
        else:
            # 没有出现过
            alpha_count[item] = 1   # 将字典的值初始化为1
            