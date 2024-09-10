list = [1,2,3,5,7,9]
target = 5


def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1

result = linear_search(list, target)
print(result)