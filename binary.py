import math


list = [1,2,3,5,7,9,10,11]
target = 11
l = 0
r = len(list) -1

while l <= r:
  mid = math.floor((l+r)/2)
  if target > list[mid]:
      l = mid +1
  if target < list[mid]:
      r= mid -1
  if(target == list[mid]):
      print(mid)
      break
      

  