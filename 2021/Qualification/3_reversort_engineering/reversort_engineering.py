#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_arr_with_cost(n,c):

    print()
    print()
    print("N: " + str(n) + ", C: " + str(c))
    
    if c < n-1:
        return "IMPOSSIBLE zu niedrig"

    max_cost = 0
    for i in range(2, n+1):
        max_cost = max_cost + i

    print("max kosten: " + str(max_cost))


    if c > max_cost:
        return "IMPOSSIBLE zu hoch"

    return("POSSIBLE")






testcases = int(input())

for caseNr in range(1, testcases + 1):

    # read input
    inp = input().split()
    n = int(inp[0])
    c = int(inp[1])

    # calculate result
    erg = get_arr_with_cost(n,c)

    print("Case #" + str(caseNr) + ": " + erg)
