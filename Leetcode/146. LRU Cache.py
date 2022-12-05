
#
# Author: minstradamuss (Loskutova Mariia)
#   

class Node:
    def __init__ (self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRU_Cache:
    def __init__ (self, capacity):
        self.capacity = capacity
        self.hashmap = dict()
        
        self.head = Node ('#', 0)
        self.tail = Node ('-', 0)

        self.head.next = self.tail
        self.head.prev = self.head

    def get (self, key):
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove (node)
            self._add (node)

            return node.val
        return -1

    def put (self, key, value):
        if key in self.hashmap:
            self._remove (self.hashmap[key])

        new_Node = Node(key, value)
        self._add (new_Node)
        self.hashmap[key] = new_Node

        if len(self.hashmap) > self.capacity:
            Node_remove = self.tail.prev
            self._remove (Node_remove)
            del self.hashmap[Node_remove.key]

    def _remove (self, node):
        prev_Node = node.prev
        next_Node = node.next
        prev_Node.next = next_Node
        next_Node.prev = prev_Node

    def _add (self, node):
        next_Node = self.head.next
        prev_Node = self.head

        prev_Node.next = node
        next_Node.prev = node

        node.next = next_Node
        node.prev = prev_Node
