class Node():
    def __init__(self, state, parent, order_added, search_type):
        # values of node to be accessed within search
        self.state = state
        self.parent = parent
        self.backward_cost = 0
        self.order_added = order_added
        self.search_type = search_type

    def get_heuristic(self):
        # uses gap heuristic as defined in "Landmark Heuristics for the Pancake Problem" by Malte Helmert."
        count = 0
        for i in range(len(self.state)-1):
            if abs(self.state[i+1] - self.state[i]) != 1:
                count += 1
        return count
    
    def total_cost(self):
        # if A* seach is selected, use heuristic in total cost
        if self.search_type == 'a':
            return self.backward_cost + self.get_heuristic()
        # if UCS search is selected, only use backwards cost
        elif self.search_type == 'u':
            return self.backward_cost
        
    
    def flip(self, level):
        # flip [level] number of pancakes
        self.state[:level] = self.state[:level][::-1] # reverse sublist
        self.level = level # so that level is accessible to print in main class
        self.backward_cost += 1 # add number of pancakes flipped to cost

    
    
    
