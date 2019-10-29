class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * capacity
    # O(n)
    def insert(self, index, value):
        '''
        Insert object before index.
        '''
        # Check if there's room in our storage
        if self.count >= self.capacity:
            # If not, return an error
            arr.double_size()

        # Shift everything to the right of index to the right
        # Start from the end to prevent overwriting values
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
            
            self.count += 1
    # O(1)
    def append(self, value):
        if self.count >= self.capacity:
            arr.double_size()
            self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        '''
        Double the storage size
        Then copy items from old storage to new
        '''
        # Double storage size
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # Copy old items to new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # Point storage to the new storage
        self.storage = new_storage
        
        
arr = DynamicArray(8)
print(arr.storage)
arr.insert(0, "z")
arr.insert(0, "y")
arr.insert(0, "x")
arr.insert(0, "w")
print(arr.storage)
arr.append("a")
arr.append("b")
arr.append("c")
arr.append("d")
print(arr.storage)
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(4)
print(arr.storage)