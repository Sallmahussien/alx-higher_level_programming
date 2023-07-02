#!/usr/bin/python3
'''Defines classes for singly linked list'''


class Node:
    '''Implement a class Node for a singly linked list'''

    def __init__(self, data, next_node=None):
        '''Initialize a new Node

        Args:
            data (int): Defines data of the new Node
            next_node (None): Defines the next of the new Node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Retrieves data of the current Node'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Set the data of the current Node'''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        '''Retrieves next_node of the current Node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Sets the next_node of the current Node'''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    '''Dedines a singly linked list'''

    def __init__(self):
        '''Initialize a new SinglyLinkedList'''
        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a new Node into the SinglyLinkedList

        Args:
            value (int): Defines the new Node inserted to the linked list
        '''
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and value > current.next_node.data:
                current = current.next_node

            if current.next_node is None:
                current.next_node = new_node
                return

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        current = self.__head
        result = ''
        while current.next_node:
            result += str(current.data) + '\n'
            current = current.next_node

        result += str(current.data)
        return result
