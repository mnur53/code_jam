import sys
import math

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)


def send_question(a, b, c):
  #eprint(str(a) + " " + str(b) + " " + str(c))
  print(str(a) + " " + str(b) + " " + str(c))
  sys.stdout.flush()
  return int(input())

def send_answer(arr):

  res = ""
  for a in arr:
    res = res + str(a) + " "

  print(res[:-1])
  sys.stdout.flush()

  inp = input()
  

def initialize_arr():

  middle = send_question(1,2,3)

  if middle == 1:
    result = [2,1,3]
  elif middle == 2:
    result = [1,2,3]
  else:
    result = [1,3,2]

  return result


def handle_2_size_arr(arr, number):
  middle = send_question(arr[0], arr[1], number)
  if middle == arr[0]:
    return [number] + arr
  elif middle == arr[1]:
    return arr + [number]
  else:
    return [arr[0]] + [number] + [arr[1]]


def handle_3_size_arr(arr, number):
  
  # check first/last
  middle = send_question(arr[0], arr[2], number)

  if middle == arr[0]:
    return [number] + arr
  elif middle == arr[2]:
    return arr + [number]

  # check inner position
  else:

    middle = send_question(arr[0], arr[1], number)
    
    if middle == arr[1]:
      return [arr[0]] + [arr[1]] + [number] + [arr[2]]
    else: 
      return [arr[0]] + [number] + [arr[1]] + [arr[2]]


def add_number_recursive(arr, number):

  # check if done? was passiert wenn 1, 2, 3 übrig?

  # wenn 2, direkte abfrage, mitte add mitte, rechts add rechts, links add links
  if len(arr) == 2:
    return handle_2_size_arr(arr, number)

  if len(arr) == 3:
    return handle_3_size_arr(arr, number)


  # wenn 4 und laenger dann rekursiv
  left_arr = arr[:int(len(arr) * 1/2)]
  right_arr = arr[int(len(arr) * 1/2):]

  middle = send_question(right_arr[0], right_arr[len(right_arr)-1], number)

  if middle == right_arr[len(right_arr)-1]:
    return arr + [number]
  elif middle == right_arr[0]:
    return add_number_recursive(left_arr, number) + right_arr
  else:
    return left_arr + add_number_recursive(right_arr, number)






inp = input().split()

t = int(inp[0])
n = int(inp[1])
q = int(inp[2])

for task in range(0, t):

  result = [1,2]

  for number in range(3, n+1):
    result = add_number_recursive(result, number)

  send_answer(result) 