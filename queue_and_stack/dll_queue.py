# added a copy of doubly_linked_list for the import
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because within the DLL node to be deleted a pointer to the prev and next node are within that node so if that pointer is known
        # time complexity is constant for that node and any number of nodes we pass in to delete O(1). With a singly linked list you only know the
        # next node and must traverse from the head to that node that is being deleted to discover the previous node value so from the head to n the node being passed in or O(n). This assumes we have the pointer to the value to be deleted.

       # self.storage with doubly linked list that we are using to implement a queue data structure
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass
