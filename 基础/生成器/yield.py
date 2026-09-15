"""
使用了yield的函数被称为生成器；
可以在迭代的过程中逐步产生值，而不是一次性返回所有结果。
生成器返回的结果就是一个迭代器。
"""

def counter(count: int):
    for i in range(count):
        yield i

c = counter(5)

print(next(c))
print(next(c))
print(next(c))
