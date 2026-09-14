import os

# 读文件：无 with 关键词
def read_file_content(file_path):
    file = open(file_path, "r")
    try:
        content = file.read()
        print(content)
    finally:
        file.close()

# 读文件：有 with 关键词
def read_file_content_with(file_path):
    with open(file_path) as file:
        content = file.read()
        print(content)


read_file_content(os.path.join(os.getcwd(), "基础/demo.txt"))
read_file_content_with(os.path.join(os.getcwd(), "基础/demo.txt"))


# with 原理
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

read_file_content_with_custom(os.path.join(os.getcwd(), "基础/demo.txt"))


# contextlib
from contextlib import contextmanager

@contextmanager
def my_file_reader(file_path):
    file = open(file_path, "r")
    yield file.read()
    file.close()

def read_file_content_with_contextmanager(file_path):
    with my_file_reader(file_path) as content:
        print(content)

read_file_content_with_contextmanager(os.path.join(os.getcwd(), "基础/demo.txt"))
