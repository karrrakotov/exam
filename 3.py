#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#   Составить программу для решения задачи: В списке, состоящем из целых элементов, вычислить:
#   1) минимальный по модулю элемент списка;
#   2) сумму модулей элементов списка, расположенных после первого элемента, равного нулю.
#   Преобразовать список таким образом, чтобы в первой его половине располагались
#   элементы, стоявшие в четных позициях, а во второй половине - элементы, стояв-шие в нечетных позициях.

if __name__ == '__main__':
    a = list(map(int, input("Введите список: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    #   Преобразовать список таким образом, чтобы в первой его половине располагались
    #   элементы, стоявшие в четных позициях, а во второй половине - элементы, стояв-шие в нечетных позициях.
    a = a[1::2] + a[0::2]
    print(a)
