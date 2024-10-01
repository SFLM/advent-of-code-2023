import time

tuples_list = [(1,2,3,4,5,6,7,8,9,10) for _ in range(1000000)]

# Using slicing
start_time = time.time()
first_items = [t[0] for t in tuples_list]
# print(first_items)
end_time = time.time()
slicing_time = end_time - start_time

# Using next()
start_time = time.time()
first_items = [next(iter(t), None) for t in tuples_list]
# print(first_items)
end_time = time.time()
next_time = end_time - start_time

# Using zip()
start_time = time.time()
first_items = [next(zip(*tuples_list))]
# print(first_items)
end_time = time.time()
zip_time = end_time - start_time

print(f"Slicing time: {slicing_time} seconds")
print(f"Next() time: {next_time} seconds")
print(f"Zip() time: {zip_time} seconds")