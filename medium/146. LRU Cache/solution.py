class LRUCache:

    def __init__(self, capacity: int):
        self.values = {}
        self.next_keys = {}
        self.prev_keys = {}
        self.capacity = capacity
        self.elements_num = 0
        self.prev_key = -1

    def get(self, key: int) -> int:
        val_out = self.values.get(key, -1)
        if val_out > -1:
            if key == self.prev_key:
                return val_out

            self.next_keys[self.prev_keys[key]] = self.next_keys[key]
            self.prev_keys[self.next_keys[key]] = self.prev_keys[key]                
            self.next_keys[self.prev_key] = key
            self.prev_keys[key] = self.prev_key
            self.prev_key = key
            return val_out           
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values[key] = value
            if key != self.prev_key:
                self.next_keys[self.prev_keys[key]] = self.next_keys[key]
                self.prev_keys[self.next_keys[key]] = self.prev_keys[key]
                self.next_keys[self.prev_key] = key
                self.prev_keys[key] = self.prev_key

        else:
            self.values[key] = value
            self.next_keys[self.prev_key] = key
            self.prev_keys[key] = self.prev_key            
            if self.elements_num >= self.capacity:
                old_lru = self.next_keys[-1]             
                self.next_keys[-1] = self.next_keys[old_lru]
                self.prev_keys[self.next_keys[-1]] = -1
                del self.next_keys[old_lru]
                del self.prev_keys[old_lru]
                del self.values[old_lru] 
            self.elements_num += 1

        self.prev_key = key


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)