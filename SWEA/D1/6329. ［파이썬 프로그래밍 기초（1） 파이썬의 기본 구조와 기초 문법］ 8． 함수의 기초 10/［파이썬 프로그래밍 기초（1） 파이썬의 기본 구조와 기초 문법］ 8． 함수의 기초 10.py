import time

def countdown(count):
    if count <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        for i in range(count):
            print(count-i)
            time.sleep(0.01)
    return

countdown(0)
countdown(10)