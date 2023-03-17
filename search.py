import copy
from node import Node

import heapq 

class Search():
    def __init__(self, unsorted_stack, search_type):
        self.unsorted_stack = unsorted_stack
        self.frontier = [] # tuples to make total cost priority
        self.visited = []
        self.order_added = 0
        self.root = Node(unsorted_stack, None, self.order_added, search_type)
        self.frontier.append((self.root.total_cost, 0, self.root))
        self.order_added += 1

    def find_duplicate(self, state):
        # check if duplicate state is already in frontier
        for tuple in self.frontier:
            if tuple[2].state == state:
                return tuple
        return None

    def expand_frontier(self, node): 
        # create children for each possible flip level 
        for level in range(2, len(self.unsorted_stack)):
            child = copy.deepcopy(node)
            child.flip(level)
            child.parent = node
            child.order_added = self.order_added
            dup = self.find_duplicate(child.state)

            # if the state is unique, push to frontier
            if (child.state not in self.visited):
                if (dup == None):
                    heapq.heappush(self.frontier, (child.total_cost(), child.order_added, child))
                    self.order_added += 1
            # use faster route to state if one is found
            elif dup != None:
                if dup[0] > child.total_cost():
                    self.frontier[self.frontier.index(dup)] = child

    def find_solution(self):
        while not len(self.frontier) == 0:
            # explore cheapest node in frontier
            node = heapq.heappop(self.frontier)[2]
            self.visited.append(node.state) # record as visited
            if node.get_heuristic() == 0: # if sorted, return sorted stack
                return node
            self.expand_frontier(node)

        


