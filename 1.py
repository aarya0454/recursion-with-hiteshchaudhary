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

def rev_string(str):
    rev_str = ''
    for char in str:
        rev_str = char+rev_str
    return rev_str

def recur_rev_str(s):
    if len(s)<1:
        return s
    else:
        return recur_rev_str(s[1:]) + s[0] 
# print(recur_rev_str('hello'))

def itr_fact(num):
    result = 1
    for i in range(2,num+1):
        result*=i
    return result
def rec_fact(num):
    if num<=1:
        return 1
    else:
        return num * rec_fact(num-1)
 