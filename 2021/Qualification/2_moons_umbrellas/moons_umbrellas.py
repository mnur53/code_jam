#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calc_min_cost(board,x,y):

    cost = 0
    last_b = board[0]
    start_index = 1

    if last_b == "?":
        for b_id, b in enumerate(board[start_index:]):
            if b != "?":
                start_index = b_id
                last_b = b
                break

    for b_id, b in enumerate(board[start_index:]):

        if last_b == "C" and b == "J":
            cost = cost + x
            last_b = b
        elif last_b == "J" and b == "C":
            cost = cost + y
            last_b = b
        else:
            pass

    return str(cost)



def calc_max_profit(board,x,y):

    cost = 0
    last_b = board[0]
    start_index = 1

    #if last_b == "?":

    
    return str(profit)


testcases = int(input())

for caseNr in range(1, testcases + 1):

    # read input
    inp = input().split()

    x = int(inp[0])
    y = int(inp[1])
    board = inp[2]

    # calculate result
    if x + y >= 1:
        erg = calc_min_cost(board,x,y)
    else:
        erg = calc_max_profit(board,x,y)

    print("Case #" + str(caseNr) + ": " + erg)


