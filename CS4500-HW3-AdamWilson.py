#https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/

import random
import math

def TSP(K, N):
    cities = []
    grid = [["[ ]" for i in range(N)] for j in range(N)] 
    for i in range(K):
        x, y = random.randrange(N), random.randrange(N)
        cities.append((x, y))
        grid[x][y] = "[X]"
    for i in range(len(grid)):
        for j in grid[i]:
            print(j, end = "")
        print()
    
    min_path = 99999
    
    while True:
        current = 0
        
        for i in range(K-1):
            current += math.sqrt(math.pow(cities[i+1][0] - cities[i][0], 2)\
            + math.pow(cities[i+1][1] - cities[i][1], 2))
        
        current += math.sqrt(math.pow(cities[K-1][0] - cities[0][0], 2)\
            + math.pow(cities[K-1][1] - cities[0][1], 2))
        
        if current < min_path:
            min_path = current
            print(cities)
        
        if not next_permutation(cities):
            break

    print(min_path)

def next_permutation(L): 
  
    n = len(L) 
  
    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]: 
        i -= 1
  
    if i == -1: 
        return False
  
    j = i + 1
    while j < n and L[j] > L[i]: 
        j += 1
    j -= 1
  
    L[i], L[j] = L[j], L[i] 
  
    left = i + 1
    right = n - 1
  
    while left < right: 
        L[left], L[right] = L[right], L[left] 
        left += 1
        right -= 1
  
    return True       
    

if __name__ == "__main__":
    K, N = 0, 0

    while K < 4 or K > 9:
        K = input("Enter the number of cities (4-9): ")
    
    while N < 10 or N > 30:
        N = input("Enter the length of the sides of the grid (10-30): ")

    TSP(K, N)
