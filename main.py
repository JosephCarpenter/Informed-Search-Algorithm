# A* Implementation of Pancake Problem
# CS131 - Artificial Intelligence

import random
from search import Search

search_type = input("Type 'a' for A* search, or 'u' for uniform cost search: ")
input_type = input("Type 'i' to input your own list, or 'r' to use a random list of 10 integers: ")
length = int(input("Enter number of elements : "))
pancakes = []
if (input_type == 'r'):
    pancakes = list(range(1, length+1))
    random.shuffle(pancakes)
elif (input_type == 'i'):
    pancakes = list(map(int,input("Enter the numbers, separated by spaces: ").strip().split()))[:length]
else:
    print("Invalid input type")

# add 11th "pancake" as plate for heuristic gap comparison
pancakes.append(length+1) 
print(pancakes[:length])

search = Search(pancakes, search_type)
solution = search.find_solution()
if solution == None:
    print("Could not find solution")
else:
    steps = []
    curr = solution
    while curr != None:
        steps.append(curr)
        curr = curr.parent
    steps.reverse()
    print("Sorting steps: ")
    print("Start:  ", pancakes[:length])
    for i in range(1, len(steps)):
                print("Step", i, ":", steps[i].state[:length], "(flipped", steps[i].level, "pancakes)")