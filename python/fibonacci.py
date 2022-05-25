from termios import NL1


def fibonacci(n):
  # Start with initializing the 2 variables
  n1 = 0
  n2 = 1
  # Set this to "" just to initialize the variable since in Python you cannot initialize without value
  next = ""

  # Case to close the recursive function
  if n == 0:
    return 0
  for idx in range(1, n):
    nextNum = n1 + n2
    n1 = n2
    n2 = nextNum
  return nextNum

