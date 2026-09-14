# with 关键词


### Python

用于上下文管理协议，简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）。

文件读写（不用 with）:

```python
# 需要手动关闭资源
# 代码冗长
def read_file_content(file_path):
  file = open(file_path, 'r')
  try:
    content = file.read()
    print(content)
  finally:
    file.close()
```

文件读写（用 with）:

```python
# 无需手动关闭资源（免得忘记）
# 代码简介
def read_file_content_with(file_path):
  with open(file_path) as file:
    print(content)
```

#### 原理

with 关键词的背后是 python 的上下文管理协议，该协议要求对象实现两个方法：

- `__enter__` 进入上下文时调用，返回值赋给 as 后的变量
- `__exit__` 退出上下文时调用，处理清理工作

自定义一个文件操作方法 `my_open`:

```python
class MyFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        file = open(self.file_path, "r")
        self.file = file
        return file.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

def read_file_content_with_custom(file_path):
    with MyFileReader(file_path) as content:
        print(content)
```

#### contextlib 模块

contextlib 模块提供了更简单的方式来创建上下文管理器：

```python
from contextlib import contextmanager

@contextmanager
def my_file_reader(file_path):
    file = open(file_path, "r")
    yield file.read()
    file.close()

def read_file_content_with_contextmanager(file_path):
    with my_file_reader(file_path) as content:
        print(content)
```



### JavaScript

JavaScript 查找某个未使用命名空间的变量时，会通过作用域链来查找，作用域链是跟执行代码的 context 或者包含这个变量的函数有关。'with'语句将某个对象添加到作用域链的顶部，如果在 statement 中有某个未使用命名空间的变量，跟作用域链中的某个属性同名，则这个变量将指向这个属性值。如果沒有同名的属性，则将拋出ReferenceError异常。

```js
const mockWindow = {
  document: {
    querySelector: (selector) => {
      console.log('From Mock Window:', selector)
    }
  }
}

with(mockWindow) {
  document.querySelector('#app')
  eval("document.querySelector('#app')")
}
```

