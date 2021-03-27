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

    return cost


results = []


for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
   
                this_arr = [a,b,c,d]
                skip = False

                for checknum in range(1,6):
                    ctr = 0

                    for this_a in this_arr:
                        if this_a == checknum:
                            ctr += 1

                    if ctr > 1:
                        skip = True

                if skip == False:
                    results.append((reversesort_with_cost(this_arr), this_arr))


sorted_by_second = sorted(results, key=lambda tup: (tup[0],tup[1]))

z_alt = 2
for r in sorted_by_second:

    if r[0] != z_alt:
        print()
        z_alt = r[0]

    print(str(r[0]) + " " + str(r[1]))

print()

print(reversesort_with_cost([2,4,3,5,1]))
print(reversesort_with_cost([2,3,5,4,1]))




def required_swaps(n, c):

    c = c - (n - 1)  
    i = 2
    print("INIT")
    print("REST " + str(c))

    while c > 0:

        if c - (n - i) > 0:
            c = c - (n - i) 
            print("NÖTIG " + str(n-i))
            print("REST " + str(c))

        i = i + 1

    

required_swaps(5,12)

"""
a = [2,3,4,5,1]
print( str(a) + " : " + str(reversesort_with_cost(a)))


a = [6,2,3,7,5,4,1]
print( str(a) + " : " + str(reversesort_with_cost(a)))





print()




print()
print()
print()

print(reversesort_with_cost([1,2,3]))
print(reversesort_with_cost([1,3,2]))
print(reversesort_with_cost([2,1,3]))
print(reversesort_with_cost([2,3,1]))
print(reversesort_with_cost([3,1,2]))
print(reversesort_with_cost([3,2,1]))


"""


# if kosten < N-1 --> IMPOSSIBLE
# if kosten > N!-1 --> IMPOSSIBLE 