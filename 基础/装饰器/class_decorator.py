# 类装饰器


# 1、函数形式类装饰器
def func_class_decorator(cls):
    class FuncClassDecorator:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.instance, name)

        def print_name(self):
            print(f"print {self.instance.name} from decorator")

    return FuncClassDecorator


@func_class_decorator
class Demo:
    def __init__(self, name):
        self.name = name


demo = Demo("Python")
demo.print_name()


# 2、类形式类装饰器
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Demo2:
    def __init__(self, name):
        self.name = name


demo2 = Demo2("Python")
demo2_2 = Demo2("Python2")
print(demo2 is demo2_2) # True
