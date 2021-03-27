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



def integrate_number_to_arr(arr, number):
  
  # init
  last_try = False

  # search correct spot
  for left_index in range(0, len(arr)):

    # udate right index
    right_index = len(arr)-1-left_index

    #eprint("arr: " + str(arr))
    #eprint("left_index: " + str(left_index))
    #eprint("right_index: " + str(right_index))

    if left_index == right_index:
      right_index += 1
      last_try = True
      #eprint("right_index ANGEPASST: " + str(right_index))

    if left_index+1 == right_index:
      last_try = True


    

    middle = send_question(arr[left_index], arr[right_index], number)

    if middle == arr[left_index]:
      #eprint("Zahl gleich links")
      arr = arr[:left_index] + [number] + arr[left_index:]
      break
    elif middle == arr[right_index]:
      #eprint("Zahl gleich rechts")
      arr = arr[:right_index+1] + [number] + arr[right_index+1:]
      break
    else:
      #eprint("Zahl mitte")
      if last_try == True:
        arr = arr[:left_index+1] + [number] + arr[left_index+1:]
        break
      pass

  #eprint("ZAHL EINGEFUEGT: " + str(arr))

  return arr


inp = input().split()

t = int(inp[0])
n = int(inp[1])
q = int(inp[2])

for task in range(0, t):

  result = initialize_arr()

  for number in range(4, n+1):
    result = integrate_number_to_arr(result, number)

  send_answer(result)



   
 