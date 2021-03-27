#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_min(arr):
    this_min = arr[0]
    del arr[0]
    return this_min, arr

def is_trouble_sort_valid(arr):

    geraden = arr[0::2]
    ungeraden = arr[1::2]
    
    geraden.sort()
    ungeraden.sort()
    
    last_min, geraden = get_min(geraden)
    index = 1

    while len(geraden) > 0 or len(ungeraden) > 0:

        if index % 2 == 0:
            this_min, geraden = get_min(geraden)
        else:
            this_min, ungeraden = get_min(ungeraden)

        if this_min >= last_min:
            last_min = this_min
            pass
        else:
            return str(index-1)

        index += 1

    return "OK"



testcases = int(input())

for caseNr in range(1, testcases + 1):

    # read input
    size = int(input())
    arr = [int(numeric_string) for numeric_string in input().split()]

    # calculate result
    erg = is_trouble_sort_valid(arr)

    print("Case #" + str(caseNr) + ": " + erg)
