#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reversesort_with_cost(arr):
    
    cost = 0

    for i in range(len(arr)-1):

        this_min = arr[i]
        this_min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < this_min:
                this_min = arr[j]
                this_min_index = j

        # reverse
        reverse_part = arr[i:this_min_index+1]
        arr = arr[:i] + reverse_part[::-1] + arr[this_min_index+1:]

        cost = cost + (this_min_index - i + 1)

    return str(cost)


testcases = int(input())

for caseNr in range(1, testcases + 1):

    # read input
    size = int(input())
    arr = [int(numeric_string) for numeric_string in input().split()]

    # calculate result
    res = reversesort_with_cost(arr)

    print("Case #" + str(caseNr) + ": " + res)