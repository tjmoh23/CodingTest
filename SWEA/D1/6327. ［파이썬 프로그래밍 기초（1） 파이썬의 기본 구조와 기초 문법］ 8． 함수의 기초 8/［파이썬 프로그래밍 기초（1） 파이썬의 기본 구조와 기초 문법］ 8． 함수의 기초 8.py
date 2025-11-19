a, b = map(int, input().split(','))

def square(a, b):
    sq_a = a**2
    sq_b = b**2
    print(f'square({a}) => {sq_a}')
    print(f'square({b}) => {sq_b}')    
    return

square(a, b)