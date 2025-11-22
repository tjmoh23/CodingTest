def ptr(num):
    nums = 1
    for i in range(1,num+1):
        nums *= i
    return nums 

a = int(input())
print(ptr(a))