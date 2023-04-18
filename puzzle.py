"""
empty tile will be represented as 0
"""
import random
import copy
import time
import numpy as np

movement = []


class node():
    def __init__(self, level, cost, state, parent, zero):
        self.level = level # level of a tree
        self.cost = cost #cost of the state
        self.state = state #state - list
        self.parent = parent # parent
        self.zero = zero

    def get_level(self):
        return self.level

    def get_cost(self):
        return self.cost

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_zero(self):
        return self.zero


class min_cost_list():
    def __init__(self):
        self.minheaplist = []

    def get_minheaplist(self):
        return self.minheaplist

    def push_minheaplist(self,new_node):
        
        insert_index = len(self.minheaplist)
        for i in range(len(self.minheaplist)):
            if new_node.get_cost() + new_node.get_level() < self.minheaplist[i].get_cost() + self.minheaplist[i].get_level():
                insert_index = i
                break
        temp_low_list = self.minheaplist[insert_index:len(self.minheaplist)]
        temp_up_list = self.minheaplist[0:insert_index]
        temp_up_list.append(new_node)
        self.minheaplist = temp_up_list + temp_low_list
        
        #for i in range(len(self.minheaplist)):
        #    print(self.minheaplist[i].get_state(), " ", self.minheaplist[i].get_cost(), " " , self.minheaplist[i].get_level())

        
    def pop_minheaplist(self):
        pop_node = self.minheaplist[0]
        self.minheaplist = self.minheaplist[1:len(self.minheaplist)]
        return pop_node

        
        

def main():
    print("hello")
    
    row_number = 3
    tile_number = row_number*row_number
    finished_puzzle = [x for x in range(tile_number)]
    finished_puzzle = finished_puzzle[1:len(finished_puzzle)]
    finished_puzzle.append(0)
    #finished_puzzle = [0,1,2,4,5,3,7,8,6]
    movement = [-row_number,row_number,-1,1]
    not_solved = True
    puz = createPuzzle(row_number)
    print(puz)
    #puz = [7,0,4,5,6,3,2,1,8] #17 steps
    if solvable(puz):
        print("solvable")
        cost = cost_calc(puz, finished_puzzle)
        zero = zero_posi(puz)
        temp_parent = node(-1,10,[0 for x in range(tile_number)],None,0)
        origin_node = node(0,cost,puz,temp_parent,zero)
        cost_list = min_cost_list()
        cost_list.push_minheaplist(origin_node)
        #time.sleep(1) 
        while(not_solved):
            print(len(cost_list.get_minheaplist()), "-", cost_list.get_minheaplist()[0].get_level())
            parent_node = cost_list.pop_minheaplist()
            p_p_puz = parent_node.get_parent().get_state()
            for v in range(4):
                if parent_node.get_zero() + movement[v] < tile_number and parent_node.get_zero() + movement[v] > -1:
                    if not((parent_node.get_zero() == 5 and v == 3) or (parent_node.get_zero() == 2 and v == 3)):
                        if not((parent_node.get_zero() == 3 and v == 2) or (parent_node.get_zero() == 6 and v == 2)):
                            new_status = copy.deepcopy(parent_node.get_state())
                            new_status[parent_node.get_zero()] = new_status[parent_node.get_zero() + movement[v]]
                            new_status[parent_node.get_zero() + movement[v]] = 0
                            if p_p_puz != new_status:

                                new_node = node(parent_node.get_level() + 1, cost_calc(new_status, finished_puzzle) + parent_node.get_level() + 1, new_status,parent_node, parent_node.get_zero() + movement[v])
                                cost_list.push_minheaplist(new_node)
                                if cost_calc(new_node.get_state(), finished_puzzle) == 0:
                                    ans_node = new_node
                                    not_solved = False

                
        
        

        #print(ans_node.get_state())
        print_step(ans_node, row_number)


    else:
        print("unsolvable")


def print_step(node, side):
    status_list = []
    cur_node = node
    npar = np.array(cur_node.get_state())
    print(npar.reshape(side,side))
    print(node.get_level())
    while(True):
        if cur_node.get_level() > 0:
            cur_node = cur_node.get_parent()
            npar = np.array(cur_node.get_state())
            print(npar.reshape(side,side))
            print(cur_node.get_level())
        else:
            break


        



def zero_posi(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            return i


def cost_calc(puzzle, finished_puzzle):
    cost = 0
    for i in range(len(puzzle)):
        if puzzle[i] != finished_puzzle[i]:
            cost += 1
    return cost
        


def createPuzzle(a_side):
    puz = [x for x in range(a_side * a_side)]
    random.shuffle(puz)
    return puz
        
def solvable(puz):
    less_posi = 0
    zero_posi = 0
    for i in range(len(puz) - 1):
        if puz[i] == 0:
            zero_posi = i
        else:
            for j in range(i+1 , len(puz)) :
                if puz[j] != 0:
                    if puz[i] > puz[j]:
                        less_posi += 1

    if len(puz)%2 == 0:
        if zero_posi%2 != 1:
            less_posi += 1
        
    if less_posi%2 == 0:
        return True
    else:
        return False


















if __name__ == "__main__":
    main()
