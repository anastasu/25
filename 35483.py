import math

for i in range (35000000,4000000):
  k=1
  if (i%2!=0): k=k+1
  A=[]
  for j in range(2,math.ceil(math.sqrt(i))):
    if (i%j==0):
      if (j%2!=0):
        k=k+1
      z= i//j
      if (z%2!=0) and (z!=j): k=k+1
  if k ==5:print(i)