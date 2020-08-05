#!/bin/python3

import math
import os
import random
import re

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep):
    while node:
        print(node.data)
        node = node.next
        if node:
            print(sep)


# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    if not head or not head.next:
        return head
    prev= None
    cur = head
    next = cur.next
    while cur:
        cur.next = prev
        cur.prev = next
        prev = cur
        cur = next
        if next:
            next = next.next
    return prev


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())
        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)


        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ')
        # fptr.write('\n')

