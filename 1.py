def sum_iterative(arr):
    total = 0
    for num in arr:
        total += num
    return total
def sum_recursion(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_recursion(arr[1:])
