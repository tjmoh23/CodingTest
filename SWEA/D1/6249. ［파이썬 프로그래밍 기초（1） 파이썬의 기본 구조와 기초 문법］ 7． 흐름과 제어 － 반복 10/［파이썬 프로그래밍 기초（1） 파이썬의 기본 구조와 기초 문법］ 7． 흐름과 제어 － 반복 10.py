n = input()

# 0~9까지 등장 횟수를 저장할 리스트
count = [0]*10 # [0, 0, 0, ..., 0]

# 입력된 문자열의 각 자리 숫자 세기
for i in n: # 문자열이라 문자 내용 그대로 들어감
    count[int(i)]+=1 # 

# 0~9 출력
for i in range(10):
    print(i, end=' ')
print()

# 각 숫자의 개수 출력
for i in count:
    print(i, end=' ')