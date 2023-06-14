# -*- encoding: utf-8 -*-

## 链表
## 链表-头插法、尾插法
## 链表的插入、删除
## 双链表的插入、删除
## 链表vs列表（索引和指针）
## 链表
# 链表是由一系列节点组成的集合，每个节点包含两部分，数据域item和指向下个节点的指针next,节点之间串联，组成一个链表。
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# print(a.next.item)
# print(a.next.next.item)


## 链表-头插法、尾插法
# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# def create_link_head(li):
#     '''
#     # 头插法
#     '''
#     head = Node(li[0]) # 列表第一个元素当作尾巴
#     for element in li[1:]:
#         node = Node(element)
#         node.next = head # 将当前节放到头节点前边
#         head = node # 当前节点作为头
#     return head
#
# def create_link_tail(li):
#     '''
#     # 尾插法
#     '''
#     head = Node(li[0]) # 头和尾巴都是第一个元素
#     tail = head
#     for element in li[1:]:
#         node = Node(element)
#         tail.next = node # 尾巴插入一个节点
#         tail = node # 这个节点变为尾巴
#     return head
#
# def print_linklist(lk):
#     while lk:
#         print(lk.item, end=',')
#         lk = lk.next # 打印下一个节点

# 头插法
# lk = create_link_head([1,2,3,4,5])
# print_linklist(lk)

# 尾插法
# lk = create_link_tail([1,2,4,5,7])
# print_linklist(lk)


## 链表的插入、删除
# 链表的插入
# p.next = curNode.next
# curNode.next = p

# 链表的删除
# p = curNode.next
# curNode.next = curNode.next.next
# del p

## 双链表的插入、删除
# 双链表的插入
# p.next = curNode.next
# curNode.next.prior = p
# p.prior = curNode
# curNode.next = p

# 双链表的删除
# p = curNode.next
# curNode.next = p.next
# p.next.prior = curNode
# del  p