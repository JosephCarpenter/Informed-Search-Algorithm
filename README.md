The Pancake Problem as a heuristic algorithm:
initial state: unsorted pile of pancakes
possible actions: number of pancakes to flip
successor function: number of pancakes to flip after first flip
goal test: whether pile is sorted by size

The heuristic function uses the gap heuristic, as defined by "Landmark Heuristics for the Pancake Problem" by Matte Helmert. It measures the number of stack positions for which the pancake at the position is more than 1 size smaller/larger from the pancake below it.

The A* search implementation uses a priority queue made of tuples containing the total cost (backwards cost + gap heuristic), order added, and the node itself. The total cost is the key deciding the order of the priority queue, and the order added decides the priority of nodes with the sam total cost. The node class represents a state configuration and amount of cost associated with the state, and the earching class visits nodes and expands the frontier. 

It takes either a user-inputted list of pancakes or a random list of pancakes of a given size. As each node is explored, the frontier expands, and the node with the lowest total cost is selected to explore next. Once a solution is found, the sequence of flips used to arrive at the sorted pancake stack is outputted. It is assumed that the input length given will match the number of elements provided, and that the elements are unique and within the values 1-length, or the program will not work properly. 

In order for the gap heuristic to work properly, an additional "pancake" (1 higher than the highest value) is added to the end of the stack to serve as the plate, so that the size difference between the last pancake and the plate can be calculated for the heuristic. The additional plate is not printed, so it isn't visible to the user.

The uniform cost search function does not use the gap heuristic, instead relying solely on the backward cost of number of flips when deciding which node to explore. As such, UCS is much slower than the A* search, and will take an unreasonably long time to run with 10 items.