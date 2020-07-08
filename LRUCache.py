class Node:
    # This is just a node of a linked list.
    def __init__(self, key,value):
        self.key  = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    """
    This is a desing of LRUCache with O(1) time complexity.
    This cache design enables users to read, write, delete or reset the cache.
    We use a dictionary for fast look up and a linked list to keep the order.

    When initializing the Cache the maximum capacity of the cache should be set.
    """

    def __init__(self, capacity):
        #initializing the head and the tail of the cache and setting up the dictionary "D"

        self.capacity = capacity
        self.D = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail # next node is pointing to tail
        self.tail.prev = self.head # previous node is pointing to head



    def get(self, key):
        if key in self.D: # check if that key is in the dictionary
            node = self.D[key]
            value = node.value
            self._remove(node)
            self._add(node)
            return value

        else:
            return -1 #if it's not in the dictionary return -1


    def put(self, key, value):
        if key in self.D:#if the key already exists we want to over write it.
            self._remove(self.D[key])
            del self.D[key]

        elif len(self.D) == self.capacity: #if we have hit the capacity of the cache remove the least recently used node.
            least_recently_used = self.head.next
            self._remove(least_recently_used)
            del self.D[least_recently_used.key]

        new_node = Node(key,value)
        self._add(new_node)
        self.D[key] = new_node

    def delete(self,key):
        if key in self.D:
            node = self.D[key]
            del self.D[key]
            self._remove(node)
        else: #if the key doesn't exists in the dictionary just return -1
            return -1

    def reset(self): #just initializing everything back to normal.
        self.D = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self,node): # this is helper function. It adds a node just before the tail.
        node.next = self.tail
        old_last_node = self.tail.prev
        old_last_node.next = node
        node.prev = old_last_node
        self.tail.prev = node

    def _remove(self, node): # this is a helper function. It removes a node from the linkedlist.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
