class Node():
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # left: LRU, Right: Most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left  
    
    # Remove node from linked list
    def remove(self, node):
        #1 -> t -> 2
        #1 <- t <- 2
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        del self.map[node.key]

    # Insert node to the right side of list
    def insert(self, node):
        #x <- right 
        x = self.right.prev

        #x <- t <- right
        node.prev = x
        self.right.prev = node

        #x -> t -> right
        x.nxt = node
        node.nxt = self.right

        # Insert into hash map
        self.map[node.key] = node
        

    def get(self, key: int) -> int:
        if key in self.map:
            # TODO: Move node to right side
            target_node = self.map[key]
            self.remove(target_node)
            self.insert(target_node)
            return target_node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # Remove old node, if exist
        if key in self.map:
            target_node = self.map[key]
            self.remove(target_node)
        # Insert new node to the right
        new_node = Node(key, value)
        self.map[key] = new_node
        self.insert(new_node)
        
        # If we go beyond capacity, remove LRU
        if len(self.map.keys()) > self.capacity:
            self.remove(self.left.nxt)

            
        
