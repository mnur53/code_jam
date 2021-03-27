#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(arr):
    erg = 0
    return str(erg)






testcases = int(input())

for caseNr in range(1, testcases + 1):

    # read input
    size = int(input())
    arr = [int(numeric_string) for numeric_string in input().split()]

    # calculate result
    erg = func(arr)

    print("Case #" + str(caseNr) + ": " + erg)
