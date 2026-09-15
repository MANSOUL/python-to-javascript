"""
迭代器是一个可以记住遍历位置的对象
从第一个元素开始访问直到最后。
"""

# 1、创建并遍历迭代器对象
list = [1, 2, 3]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        print("end")
        break


# 2、实现一个迭代器
class Counter:
    def __init__(self, count: int):
        self.count = count
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        current = self.index
        if (current < self.count):
            self.index += 1
            return current
        else:
            raise StopIteration

counter = Counter(5)
while True:
    try:
        print(next(counter))
    except StopIteration:
        print("counter end")
        break

# for i in counter:
#     print(i)

