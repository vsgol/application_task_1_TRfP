import sys as __sys


def print_vars():
    frame = __sys._getframe(1)
    for key, val in frame.f_locals.items():
        if not key.startswith('_') and not hasattr(val, '__call__'):
            print(key, ': ', val.__class__.__module__ == 'builtins')


if __name__ == '__main__':
    class MyClass:
        a = 1

    def foo():
        aa = 1
        cc = [1, 2, 3]
        bsa = MyClass()
        aaw = __sys.stdin
        print("Локальные пееременные функции foo")
        print_vars()


    a = 1
    b = 2
    c = [1, 2, 3]
    d = 'asd'
    bs = MyClass()
    bf = __sys.stdin
    foo()
    print("Локальные пееременные функции main")
    print_vars()
