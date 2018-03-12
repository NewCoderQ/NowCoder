# -*- coding: utf-8 -*-
# 保留最大数

from __future__ import print_function
import sys

src_value = raw_input()        # 获取输入的数值
count = int(raw_input())            # 获取需要删除的数字个数，并且将其转换成 int 类型

int_value_list = [i for i in src_value]    # 将输入的元素转换成的列表

# 定义一些变量
new_result_index = delete_count = 0    # 第一个变量为结果列表的索引，第二个变量为已经删除的数字数量
result_list = [0] * (len(int_value_list) - count)                    # 定义一个结果列表，用来存放最后的保留下来的结果数字

# 定义一个外循环，用来遍历输入值的每一位数字
for i in range(len(int_value_list)):            # 获取每一位的数值
    while new_result_index > 0 and int(result_list[new_result_index - 1]) < int(int_value_list[i]) and delete_count < count:
        delete_count += 1
        new_result_index -= 1
        # print(new_result_index, end='')
    if new_result_index < len(int_value_list) - count:
        result_list[new_result_index] = int_value_list[i]
        # print(result_list)
        new_result_index += 1
print(''.join(result_list))
    