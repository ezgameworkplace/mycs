# -*- coding: utf-8 -*-
"""
File:quick_maths.py
Author:ezgameworkplace
Date:2023/3/1
"""
"""
引用类型+作用域
"""

def add(a):
    for i in a:
        i += 1
        print(f"inside for statement::: i:{i}")


def temp_add(a):
    for i in range(len(a)):
        a[i] += 1


def swap(a, b):
    temp = b
    b = a
    a = b
    print(f"inside swap:::  a:{a},b:{b}")


if __name__ == '__main__':
    a = [1, 2, 3]
    add(a)
    print('add a', a)

    temp_add(a)
    print('temp_add a', a)

    a = 1
    b = 2
    swap(a, b)
    print(f"outside swap:::  a:{a},b:{b}")
