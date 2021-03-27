import math
print(math.ceil(4.2))




def check_sub_array(arr, number):

    left_arr = arr[:int(len(arr) * 1/2)]
    right_arr = arr[int(len(arr) * 1/2):]

    print(left_arr)
    print(right_arr)



#arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
num = 5


print("TEST 7")
arr = [1,2,3,4,5,6,7]
check_sub_array(arr,num)

print("TEST 6")
arr = [1,2,3,4,5,6]
check_sub_array(arr,num)

print("TEST 5")
arr = [1,2,3,4,5]
check_sub_array(arr,num)


print("TEST 4")
arr = [1,2,3,4]
check_sub_array(arr,num)


print("TEST 3")
arr = [1,2,3]
check_sub_array(arr,num)








