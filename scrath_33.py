a = lambda x: x + 1
print('Type of a:', type(a))
assert a(1) == 2


b = lambda x, y: x + y
print('Type of b:', type(b))
assert b(1, 2) == 3


c = lambda my_list: [element // 2 for element in my_list]
assert c([2, 4, 6]) == [1, 2, 3]


d = lambda func, *args, **kwargs: func(*args, **kwargs)
print(d(c, [4, 6, 8]))