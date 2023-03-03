# -*- coding: utf-8 -*-
"""
File:static_books.py
Author:ezgameworkplace
Date:2023/3/3
"""
"""
实例变量/方法+类变量/方法(静态变量/方法)
"""
from collections import deque


class Book:
    last = None

    def __init__(self, title):
        self.title = title
        self.library = None
        Book.last = self

    @staticmethod
    def last_book_title():
        if Book.last == None:
            raise Exception("null pointer error")
        return Book.last

    def get_title(self):
        return self.title


class Library:
    totalBooks = 0

    def __init__(self, size):
        self.books = deque(maxlen=size)  # python中使用deque（双端队列） 来限制列表的长度
        self.index = 0

    def add_book(self, book):
        self.books.append(book)
        self.index += 1
        Library.totalBooks += 1
        book.library = self


if __name__ == '__main__':
    '''
    Question A:
    1. Change the totalBooks variable to non static
    2. Change the lastBookTitle method to non static
    3. Change the addBook method to static
    4. Change the last variable to non static
    5. Change the library variable to static
    
    ANSWER:T/T/F/F/T
    '''

    print("核心：类在实例前创建，类变量和类方法中不可以引用实例变量和实例方法")
    print("1.total_books类变量只在实例方法中使用过，可以改成实例变量")
    print("2.last_book_title类方法改成实例方法永远都不会报错")
    print("3.addbook实例方法不可以变成类方法，因为books和index是实例变量")
    print("4.last类变量在类方法last_book_title中引用了，所以不可以变成实例变量,想变成实例必须把类方法也变成实例")
    print("5.library类变量可以变成实例变量，因为add_book是实例方法")

    print("\n总结：实例变量/方法可以引用在类变量/方法中，反之类不可以调用实例的变量/方法")
    print("\n下表表示：横列引用竖行")
    print("\t  || 实例 ||  类  |\n| 实例 || True|| False|\n|  类 || True || True |\n")

    '''
    Question B: 略
    '''
