a = 3
b = -1
c = 4
d = 7
e = 0.5

def solution_station_7(equation, a, b, c, d, e):
    
    result = eval(equation, {'a': a, 'b': b, 'c': c, 'd': d, 'e': e})
    return result
    
user_equation = input("Enter your equation:")

result = solution_station_7(user_equation, a, b, c, d, e)

print(f"Result: {result}")
    