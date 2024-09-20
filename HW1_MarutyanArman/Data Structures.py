import queue

"Create a list of integers and add 5 elements to it."
# l1 = [0, 1, 2, 3]
# l1.extend([4, 5, 6, 7, 8])
# print(l1)


"Create a dictionary with string keys and integer values, and add 5 key-value pairs to it."
# d = {}
# def create_dict(d_key, d_value):
#     # check whether key's type is string and value is integer
#     if isinstance(d_key, str) and isinstance(d_value, int):
#         d[d_key] = d_value
#     else:
#         print("Key: {} or/and Value: {} don't correspond to the format".format(d_key, d_value))
#
# create_dict("key1", 1)
# create_dict("key2", 2)
# create_dict(45, "value1")
# create_dict("key3", 3)
# create_dict("key4", 4)
# create_dict(True, 1.4)
# create_dict("key5", 5)
# print(d)

"Create a queue of integers and add 5 elements to it."
# q = queue.Queue()
# for i in range(5):
#     q.put(i)
#
# print("The queue elements are: ", end="")
# while not q.empty():
#     print(q.get(), end=' ')


"Create a stack of integers and add 5 elements to it."
# st = queue.LifoQueue()
# for i in range(5):
#     st.put(i)


