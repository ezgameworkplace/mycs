# -*- coding: utf-8 -*-
"""
File:switcheroo.py
Author:ezgameworkplace
Date:2023/2/28
"""
"""
值类型vs引用类型
"""

class Foo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def switcheroo(a, b):
    temp = a
    a = b
    b = temp


def fliperoo(a, b):
    temp = Foo(a.x, a.y)
    a.x = b.x
    a.y = b.y
    b.x = temp.x
    b.y = temp.y


def swaperoo(a, b):
    temp = a
    a.x = b.x
    a.y = b.y
    b.x = temp.x
    b.y = temp.y


def _print_xy(foo: Foo, bar: Foo):
    print("====================================分割线====================================")
    print(foo.x)
    print(foo.y)
    print(bar.x)
    print(bar.y)


if __name__ == '__main__':
    foo = Foo(10, 20)
    bar = Foo(30, 40)

    switcheroo(foo, bar)
    _print_xy(foo, bar)

    fliperoo(foo, bar)
    _print_xy(foo, bar)

    swaperoo(foo, bar)
    _print_xy(foo, bar)
