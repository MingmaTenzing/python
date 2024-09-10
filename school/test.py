import math

list = list(input('enter your list'))
target = int(input ('give me your target'))
left=0 
right = len(list)-1



while left <=right:
    mid = math.floor((left + right)/2)
    if(list[mid] == target):
        print(f"{target} is {mid}")
        break
    if(list[mid] < target):
        left = mid  +1 
    else: 
        right = mid -1
