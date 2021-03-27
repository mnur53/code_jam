import sys
import math

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_score_of_3x3(field,i,j):
  return sum(field[i-1][j-1:j+2]) + sum(field[i][j-1:j+2]) + sum(field[i+1][j-1:j+2])

def get_min_field_score(field):

  min_score = 10
  i = -1
  j = -1

  for i in range(1, len(field)-1):
    for j in range(1, len(field[i])-1):
      calc_score = get_score_of_3x3(field,i,j)

      if calc_score == 0:
        return i, j

      if min_score > calc_score:
        min_score = calc_score
        min_i = i
        min_j = j

  return min_i, min_j


def print_field(field):
  for f in field:
    for f2 in f:
      eprint(f2, end='')
    eprint()


t = int(input())        #// reads 2 into t


for case_number in range(1, t+1):

  a = int(input())         #// reads 3 into a

  sqrt_a = math.sqrt(a)

  num_i = int(sqrt_a)
  num_j = int(sqrt_a) + 1

  field = []
  for i in range(0, num_j):
    field.append(num_i * [0])


  x = 0
  while x > -1:

    target_i, target_j = get_min_field_score(field)

    print(str(target_i+1) + " " + str(target_j+1))
    sys.stdout.flush()

    msg = input()

    x, y = msg.split(" ")

    x = int(x)-1
    y = int(y)-1

    if x == -1:
      continue  

    # update field
    field[x][y] = 1

 