#!/bin/python3

import math
import os
import random
import re
import sys
from dotenv import load_dotenv

load_dotenv()


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


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if not head:
        return new_node
    if data <= head.data:
        head.prev = new_node
        new_node.next = head
        return new_node
    new_head = head
    while head.next is not None and head.next.data < data:
        head = head.next
    print(head.data)
    if not head.next:
        head.next = new_node
        new_node.prev = head
    else:
        new_node.next = head.next
        head.next.prev = new_node
        head.next = new_node
        new_node.prev = head
    return new_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
