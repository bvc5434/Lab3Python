# Author: Brendan Corso bvc5434@psu.edu
# Collaborator: Christopher McKinney cmm8086@psu.edu
# Collaborator: Mason McGuirk mtm5868@psu.edu
# Collaborator:Zi han Xia zfx5078@psu.edu
# Section: 004R
# Breakout: 14

def sum_n(n):
  if (n == 0):
    return 0
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if (n == 0):
    return
  else: 
    print(s)
    print_n(s, n-1)

def run():
  nv = int(input("Enter an int: "))
  print(f"sum is {sum_n(nv)}.")
  sv = input("Enter a string: ")
  print_n(sv,nv)

if __name__ == "__main__":
  run()