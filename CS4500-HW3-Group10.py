#TITLE: TSP Solution
#FILE: CS4500-HW3-Group10.py
#EXTERNAL FILES NEEDED: none
#EXTERNAL FILES CREATED: none
#PROGRAMMERS: James Brown, Safiullah Khan, Eva Roeder, Adam Wilson
#EMAIL ADDRESSES: adwzq4@gmail.com
#COURSE NUMBER: CS4500-01
#DATE: 2/28/2020
#DESCRIPTION: This program finds the solution to the Travelling Salesperson Problem
#   by iterating through every permutation of a list of "cities" located on an (x,y) grid.
#   Each permutation represents a possible path through the cities. The distance between each
#   city on a path is summed, and the minimum sum is stored. Each time a new minimum is found,
#   the corresponding path is displayed.
#RESOURCES USED:
#   https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
#   https://www.geeksforgeeks.org/permutation-and-combination-in-python/

import random
import math
from itertools import permutations

#travelling salesperson problem function, takes number of cities and gridsize as parameters
def TSP(K, N):
    cities = []
    grid = [["[ ]" for i in range(N)] for j in range(N)]

    #randomly locates K cities on an NxN grid, then displays that grid
    for i in range(K):
        x, y = random.randrange(N), random.randrange(N)
        cities.append((x, y))
        grid[x][y] = "[X]"
    for i in range(len(grid)):
        for j in grid[i]:
            print(j, end = "")
        print()
    
    min_path = 99999

    #creates a list of every permutation of the cities list
    perm = permutations(cities)

    #iterates through each list of cities
    for city in perm:
        current = 0

        #calculates and sums the magnitudes of each vector in this path
        for i in range(K-1):
            current += math.sqrt(math.pow(city[i+1][0] - city[i][0], 2)\
            + math.pow(city[i+1][1] - city[i][1], 2))
        
        current += math.sqrt(math.pow(city[K-1][0] - city[0][0], 2)\
            + math.pow(city[K-1][1] - city[0][1], 2))

        #stores minimum path length and prints each new shortest path
        if current < min_path:
            min_path = current
            print("New shortest path:")
            for i in range(K):
                print(city[i], end=" -> ")
            print (city[0])
        
    print("Minimum path length: {}".format(min_path))

#main program driver takes user input for number of cities and grid size
if __name__ == "__main__":
    K, N = 0, 0

    #validates that number of cities is between 4 and 9, inclusive
    while K < 4 or K > 9:
        K = int(input("Enter the number of cities (4-9): "))
    #validates that square grid dimension(s) is between 10 and 30, inclusive
    while N < 10 or N > 30:
        N = int(input("Enter the length of the sides of the grid (10-30): "))

    TSP(K, N)
