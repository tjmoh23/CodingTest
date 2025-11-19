def square(n):
    return n * n

# 입력: "2, 3"
nums = input().split(',')

for num in nums:
    n = int(num.strip())     # 공백 제거 + 정수 변환
    print(f"square({n}) => {square(n)}")