"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # Adds to head a value and reassigns next value with a pointer to previous head value and previous head has prev pointer to new node being added
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        # increase length and if no nodes make this node the head and tail if not true make this new node the head and assign head to be
        # next of this new_node
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # If there is a head already assign this new head as the head value and previous head will have a pointer as a net
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return new_node

    def remove_from_head(self):
        # This will allow you to return removed head value later
        value = self.head.value
        # Performs reassignment of next value to None or null effectively removing it from the doubly linked list
        self.delete(self.head)
        return value
    # Add length to list reassign new node to tail and update pointers on old tail

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    # remove node input from current position and place it at the head

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
    # does same as move to front with tail value

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
    # Shrink link of list by 1, replace head with node after current head if node passed in is the head and handle case if node was tail

    def delete(self, node):
        if self.length:
            self.length -= 1
            if node == self.head:
                self.head = node.next
            if node == self.tail:
                self.tail = node.prev
            node.delete()
        # Handles case where there are no items in this list to delete
        else:
            raise Exception('There are no items in this list to delete!')
    # Return highest value in the list get the value of the node head iterate through next values if any value is greater make that the new max value

    def get_max(self):
        node = self.head
        max_value = node.value
        while node.next:
            node = node.next
            if node.value > max_value:
                max_value = node.value
        return max_value
