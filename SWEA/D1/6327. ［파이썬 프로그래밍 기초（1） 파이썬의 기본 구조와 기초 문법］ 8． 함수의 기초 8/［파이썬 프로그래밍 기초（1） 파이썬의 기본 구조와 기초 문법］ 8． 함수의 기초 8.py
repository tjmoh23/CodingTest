def square(n):
    return n * n

# 입력: "2, 3"
nums = input().split(',')

for num in nums:
    n = int(num.strip())     # 공백 제거 + 정수 변환
    print(f"square({n}) => {square(n)}")



'''
# 이건 끼워 맞ㅊ기
a, b = map(int, input().split(','))
 
def square(a, b):
    sq_a = a**2
    sq_b = b**2
    print(f'square({a}) => {sq_a}')
    print(f'square({b}) => {sq_b}')    
    return
 
square(a, b)

'''
