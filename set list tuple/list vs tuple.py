# list are mutable while tuples are immutable

# tuple occupy less memory than list
import sys


list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)




print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple1), "bytes")

# OUTPUT:
# 104 bytes
# 80 bytes


# time efficiency
import time
import platform

print(platform.python_version())

start_time = time.time()
list2 = list(range(10000000))
end_time = time.time()
print("Time taken to create list: ", end_time - start_time, "seconds")

start_time2 = time.time()
tuple2 = tuple(range(10000000))
end_time2 = time.time()
print("Time taken to create tuple: ", end_time2 - start_time2, "seconds")

start_time3 = time.time()
for item in list2:
    listItem = list2[20000]

end_time3 = time.time()
print("Time taken to access list: ", end_time3 - start_time3, "seconds")

start_time4 = time.time()
for item in tuple2:
    tupleItem = tuple2[20000]

end_time4 = time.time()
print("Time taken to access tuple: ", end_time4 - start_time4, "seconds")

# OUTPUT:
# 3.11.5
# Time taken to create list:  0.2461867332458496 seconds
# Time taken to create tuple:  0.32172727584838867 seconds
# Time taken to access list:  1.5421621799468994 seconds
# Time taken to access tuple:  1.2596120834350586 seconds
