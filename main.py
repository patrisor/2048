import random

# Kills program 
def die(inp):
  if inp == "q":
    exit(-1)

# TODO: UPDATE GUI
def print_grid(g):
  for r in range(len(g)):
    print(g[r])

def add_random(g):
  values = [2, 4]
  while True:
    r1 = random.randint(0, 3)
    r2 = random.randint(0, 3)
    if g[r1][r2] == 0:
      g[r1][r2] = values[random.randint(0, 1)]
      break
    continue

def move(g):
  for r in range(len(g)):
    for c in range(len(g[r])):
      if g[r][c] 

# TODO: Update Grid based on input
def update_grid(g, inp):
  add_random(g)
  if inp == "w":
    print("Move up")
    # Check for 
  elif inp == "a":
    print("Move left")
  elif inp == "s":
    print("Move down")
  else:
    print("Move right")
    move(g)

# Input parser
def parse_input():
  while True:
    ret = input("Use W, A, S, or D to move the tiles.\n").lower()
    if die(ret) or (ret != "w" and ret != "a" and ret != "s" and ret != "d"):
      print("Invalid Input. Try Again")
      continue
    return ret

# Initializes the current state of our grid
def init_grid():
  values = [2, 4]
  ret = [[0] * 4 for _ in range(4)]
  ret[random.randint(0, 3)][random.randint(0, 3)] = values[random.randint(0, 1)]
  ret[random.randint(0, 3)][random.randint(0, 3)] = values[random.randint(0, 1)]
  return ret

'''TODO: DELETE'''
def test_slider():
  return [2, 0, 4, 0]

# DELETE
test = test_slider()

GRID = init_grid()
highscore = 0
score = 0
print("Join the numbers and get to the 2048 tile!")
while True:
  #print_grid(GRID)
  print(test)
  
  inp = parse_input()
  
  #update_grid(GRID, inp)
