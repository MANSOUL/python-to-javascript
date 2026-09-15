# 装饰器是一个函数，接受函数作为参数，并返回一个函数，用于增强原函数


# 1、普通函数装饰器
def decorator(original_func):
    """装饰器示例"""

    def wrapper(*args, **kwargs):
        print("原函数执行前")
        original_func(*args, **kwargs)
        print("原函数执行后")

    return wrapper


@decorator
def print_a_message_1(message: str):
    print(f"print a message: {message}")


print_a_message_1(message="Hello Python!")


# 2、带参数的函数装饰器
def decorator_with_args(times: int):
    def decorator(original_func):
        def wrapper(*args, **kwargs):
            print("原函数执行前")
            for i in range(times):
                original_func(*args, **kwargs)
            print("原函数执行后")

        return wrapper

    return decorator


@decorator_with_args(3)
def print_a_message_2(message: str):
    print(f"print a message: {message}")


print_a_message_2(message="Hello Python!")
