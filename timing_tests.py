import time

# O(n^2)
def add_to_front(n):
    x = []
    for i in range(0, n):
        x.insert(0, n - i)
    return x

# O(n)
def add_to_back(n):
    x = []
    for i in range(0, n):
        x.append(i + 1)
    return x

# O(n)
def pre_allocate(n):
    x = [None] * n
    for i in range(0, n):
        x[i] = i + 1
    return x

n = 1000000

start_time = time.time()
add_to_back(n)
end_time = time.time()
print(f"add to back runtime: {end_time - start_time} seconds")

# start_time = time.time()
# add_to_front(n)
# end_time = time.time()
# print (f"add to front runtime: {end_time - start_time} seconds")
# ​
start_time = time.time()
pre_allocate(n)
end_time = time.time()
print (f"preallocate runtime: {end_time - start_time} seconds")