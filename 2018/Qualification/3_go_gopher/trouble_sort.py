#!/usr/bin/env python
# -*- coding: utf-8 -*-

def einordnen(zahl:int, arr:[int]):

    for i in range(0, len(arr)):
        if arr[i] > zahl:
            return arr[:i] + [zahl] + arr[i:]

    return arr + [zahl]


def erstelle_listen(arr):
    gerade_sortiert = []
    ungerade_sortiert = []

    for i in range(0, len(arr), 2):
        gerade_sortiert = einordnen(arr[i], gerade_sortiert)

    for i in range(1, len(arr), 2):
        ungerade_sortiert = einordnen(arr[i], ungerade_sortiert)

    return gerade_sortiert, ungerade_sortiert


def einlesen(gerade_sortiert, ungerade_sortiert):

    laenge = len(gerade_sortiert) + len(ungerade_sortiert)
    fehler_index = 0
    read_index = 0

    last_num = -1

    for i in range(0,laenge):

        if i % 2 == 0:
            if last_num > gerade_sortiert[read_index]:
                return str(i-1)
            last_num = gerade_sortiert[read_index] 
        else:
            if last_num > ungerade_sortiert[read_index]:
                return str(i-1)
            last_num = ungerade_sortiert[read_index]
            read_index = read_index + 1

    return "OK"





testcases = int(input())

for caseNr in range(1, testcases + 1):

    size = int(input())
    arr = [int(numeric_string) for numeric_string in input().split()]


    a, b = erstelle_listen(arr)
    erg = einlesen(a,b)

    print("Case #" + str(caseNr) + ": " + erg)

