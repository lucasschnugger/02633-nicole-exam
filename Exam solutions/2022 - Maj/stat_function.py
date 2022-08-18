import numpy as np
def stat_function(x,k,t):
  if k == 0:
    return 1
  result=1
  if t == 'rising':
    for i in range(k):
      result*=(x+i)
  elif t=='falling':
    for i in range(k):
      result*=(x-i)

  return result
print(stat_function(4,3,'falling'))
