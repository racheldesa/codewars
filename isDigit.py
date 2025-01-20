import re

"""
Returns True if string n is comprised of a single digit 0-9
Returns False otherwise
"""
def is_digit(n):
  if len(n) > 1:
    return False
  else:
    result = re.search("\d",n)
    if result:
      return True
    else:
      return False
