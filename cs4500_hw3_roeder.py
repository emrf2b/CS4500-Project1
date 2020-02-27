"""
CONTRIBUTORS: James Brown ()
              Safi Khan ()
              Eva Roeder (emrf2b@mail.umsl.edu)
              Adam Wilson ()
PROJECT NAME: 





https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly

https://stackoverflow.com/questions/11858159/displaying-python-2d-list-without-commas-brackets-etc-and-newline-after-every
"""
from itertools import permutations
import collections
import math
from random import seed
from random import randint
seed(4500)

def user_pick_num_cities():

    k = int(input("Please enter the number of cities the salesman will visit. \n" +
                  "Entries must be between 4 nd 9, inclusive. \n"))
    while(k < 4 or k > 9):
        print("Only enter an integer value of 4, 5, 6, 7, 8, or 9:")
        k = int(input("Please re-enter a value for k: \n"))
    return k

def user_pick_grid_len():
    n = int(input("Please enter the length of one side of the grid the salesman \n"+
                  "will be traveling on. \n"+
                  "Entries must be between 10 and 30, inclusive. \n"))
    while(n < 10 or n > 30):
        print("Only enter an integer value between 10 and 30, including 10 and 30:")
        n = int(input("Please re-enter a value for n: \n"))
    return n

def get_coordinates(k, n):
    city_coords = []
    
    for cities in range(k):          
        x, y = randint(0, n), randint(0, n)
        city_coords.append((x, y))
    
    print("\nCOORDINATES")
    print(*city_coords)
    return city_coords

def create_grid(city, k, n):
    rows, cols = (n, n)
    grid = [['.']*cols for _ in range(rows)] 
    
    for i in range(k):
       for row, col in city:       
           if (row, col) != city[i]:
               continue
           else:
                grid[row-1][col-1] = i
                continue

    print("\nGRID")
    for row in grid:
        print (" ".join(map(str,row)))           
    
def find_distances(coords, k):
    rows, cols = (k, k)
    dist_matrix = [[99]*cols for _ in range(rows)]
    matrix = [[99]*cols for _ in range(rows)]
    
    list_x = []
    list_y = []
    for x, y in coords:
        list_x.append(x)
        list_y.append(y)
    
    Dict_of_coords = collections.OrderedDict()
    [Dict_of_coords.setdefault(i, coords[i]) for i in range(0, len(coords))]
    
    for key, values in Dict_of_coords.items():
        for i in range(k):
            if matrix[key][i] == 99:
                num = math.sqrt( (list_x[key] - list_x[i])**2 + (list_y[key] - list_y[i])**2 )
                dist_matrix[key][i] = math.sqrt( (list_x[key] - list_x[i])**2 + (list_y[key] - list_y[i])**2 )
                matrix[key][i] = "{0:.2f}".format(num)
            else:
                continue
    
    print("\nDISTANCE MATRIX")
    for row in matrix:
        print (" ".join(map(str,row)))
        print("\t\t")          
        
    return dist_matrix

def calc_shortest_route(d_mat, k, n):
    numbers = []    
    for i in range(1, k):
        numbers.append(i)
            
    perms = permutations(numbers)
    perm_list = []
    for i in list(perms):
        perm_list.append(list(i))

    combos = []
    for i in perm_list:
        i.append(0)
        i.insert(0, 0)
        combos.append(i)
    
    temp = -1
    counter = 0
    shortest = 10000
    for combo in combos:
        temp += 1
#        print("\nCurrent Route: ", combo)
        temp_dist = 0
        for i in range(k):
            temp_dist += d_mat[combo[i]][combo[i+1]]
#        print("Current Distance: ", temp_dist)
            
        if temp_dist < shortest:
            shortest = temp_dist
            counter = temp
#            print("Current Shortest: ", shortest)
            
    
    optimal_route = combos[counter]
    
    print("OPTIMAL ROUTE")
    print("The shortest route is ") 
    print(optimal_route)
    print("with a distance of ")
    print(shortest)
    
############### MAIN ################
k = user_pick_num_cities()
n = user_pick_grid_len()


city_coords = get_coordinates(k, n)

#Show the cities on a grid
create_grid(city_coords, k, n)

dist_matrix = find_distances(city_coords, k)

calc_shortest_route(dist_matrix, k, n)