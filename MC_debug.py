import numpy as np
def MC(i: np.array ):
  denominator = 3 ** len(i)

  sum_1 = 0
  for h in range(1, len(i) + 1):
    sum_1 += mu(i[:h])

  sum_2 = 0
  for r in range(1, len(i) + 1):
    sum_3 = 0
    for z in range(1, len(i) + 1 - r):
      sum_3 += mu(i[:len(i) + 1 - z])
    sum_2 += (2**sum_3) * (3 ** (r -1))

  return ((2**sum_1) - sum_2)/denominator

def mu(i: np.array):
  if len(i) == 1:
    return 2*i[-1]
  else:
    return 2*i[-1] - (MC(i[:-1]) % 3) + 1 


man = np.array([3], dtype = int)
print(MC(man))