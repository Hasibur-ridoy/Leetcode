class Node:
    def __init__(self, key, val):
        self.key , self.val = key, val
        self.prev , self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #this is the hash map
        self.left, self.right = Node (0,0) , Node(0,0) # dummy pointers for doubly linklist

        # pointing towards other node that's between them
        #left pointer is going to help us find the least used key, val pair
        #right pointer is going to help us find the most used key, val pair
        self.left.next, self.right.prev = self.right, self.left

    """" To remove least used val from left pointer """
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)