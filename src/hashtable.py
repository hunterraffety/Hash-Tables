# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        '''

        '''
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #provide integer index from the hash method with a given key
        index = self._hash_mod(key)
        print(key)
        #create a new node with linkedpair when method is invoked using the key and value
        node = LinkedPair(key, value)
        print(f"key, {key}, value, {value}")
        #we need to attach it a next property that uses storage to dip it into a bucket
        node.next = self.storage[index]
        #now we can swap
        self.storage[index] = node
        print(f"node: {node}")



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        #check in storage to see if the key is there
        if self.storage[index] is None:
            print("Not there")

        #make remove the has, then attach it to next
        remove = self.storage[index]
        self.storage[index] = remove.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #print(f"index: {index}")
        #check for value
        #if self.storage[index] == key
            #set to a var curr_pair to self.storage;
            #begin while for current_pair:
            #iterate through and check curr_pair[key] to == key
            #then return the value of curr_pair
            #curr.pair to curr.next
        
        index = self._hash_mod(key)
        
        current_pair = self.storage[index]

        while current_pair:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #capacity holds the amount of storage, so by looping through it, we can append and for it to rehash the table by triggering it again
        for i in range(self.capacity):
            self.storage.append(None)



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
