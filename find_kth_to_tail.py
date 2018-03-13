# -*- coding: utf-8 -*-
# @Author: qiaozhiqiang01
# @Date:   2018-03-13 15:33:18
# @Last Modified by:   qiaozhiqiang01
# @Last Modified time: 2018-03-13 15:33:55

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None:
            return head
        else:
            count = 0        # 定义一个计数变量，用来统计链表中结点的个数
            node_list = list()        # 创建一个结点列表
            while head != None:        # 不是最后一个结点
                count += 1
                node_list.append(head)        # 将当前结点添加进列表中
                head = head.next              # 指向下一个结点
            
            if k == 0:
                return None
            elif count < k:
                return None
            else:
                return node_list[count - k]