
def solution_station_1(n):
    fibonnaci = [0, 1]
    for i in range (1, n):
        fibonnaci.append(fibonnaci[i] + fibonnaci[i-1])
    
    return fibonnaci[n]

