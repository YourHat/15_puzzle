"""
empty tile will be represented as 0
"""
import random #randomized puzzle
import copy # for deepcopy
import numpy as np #for output

class node():
    """
    class for each node in min heap
    """
    def __init__(self, level, cost, state, parent, zero):
        self.level = level # level of a tree
        self.cost = cost #cost of the state
        self.state = state #state - puzzle state list
        self.parent = parent # parent
        self.zero = zero #index of empty tile

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
    """
    min heap
    """
    def __init__(self):
        self.minheaplist = []

    def get_minheaplist(self):
        return self.minheaplist

    def push_minheaplist(self,new_node):
        """
        add new node to the minheap
        """
        insert_index = len(self.minheaplist)
        for i in range(len(self.minheaplist)):
            if new_node.get_cost() + new_node.get_level() < self.minheaplist[i].get_cost() + self.minheaplist[i].get_level():
                insert_index = i
                break
        temp_low_list = self.minheaplist[insert_index:len(self.minheaplist)]
        temp_up_list = self.minheaplist[0:insert_index]
        temp_up_list.append(new_node)
        self.minheaplist = temp_up_list + temp_low_list
        
        
    def pop_minheaplist(self):
        """
        pop the first item in the minheap
        """
        pop_node = self.minheaplist[0]
        self.minheaplist = self.minheaplist[1:len(self.minheaplist)]
        return pop_node
         

def main():
    
    while True: # loop menu
        r_t = input("type 'r' for random puzzle, 't' for test puzzle, 'd' to close : ")

        if r_t == 'r': #random puzzle
            p_type = input("type a number of column : ")
            solve_puzzle(int(p_type),createPuzzle(int(p_type)))

        elif r_t == 't': # test cases
            test_num = input("type number of test you want to test\n1)2x2 - 2 steps \n2)2x2 - 5steps \n3)3x3 - 17 steps\n4)3x3 - 19 steps\n5)4x4 - 2 steps\n6)4x4 - 5 steps\n7)4x4 - 7 steps\n8)4x4 - 9 steps\n9)4x4 - 14 steps\n10)4x4 - 18 steps\n11)5x5 - 17 steps\n12)6x6 - 16 steps\n -> ")
            match int(test_num):
                case 1:
                    solve_puzzle(2,[0,1,3,2])
                case 2:
                    solve_puzzle(2,[0,2,1,3])
                case 2:
                    solve_puzzle(3, [7,0,4,5,6,3,2,1,8])
                case 4:
                    solve_puzzle(3, [8,7,1,0,2,3,6,5,4])
                case 5:
                    solve_puzzle(4,[1,2,3,4,5,6,7,8,9,10,0,11,13,14,15,12])
                case 6:
                    solve_puzzle(4,[1,0,3,4,5,2,7,8,9,6,11,12,13,10,14,15])             
                case 7:
                    solve_puzzle(4,[1,2,3,4,0,10,6,7,5,9,11,8,13,14,15,12])       
                case 8:
                    solve_puzzle(4,[1,6,2,4,9,5,3,8,13,10,7,12,0,14,11,15])       
                case 9:
                    solve_puzzle(4,[5,1,3,4,2,7,8,12,9,6,11,10,13,0,14,15])   
                case 10:
                    solve_puzzle(4,[2,3,6,7,1,10,12,4,5,11,0,8,9,13,14,15])   
                case 11:
                    solve_puzzle(5,[1,3,8,4,5,6,2,13,9,0,11,7,17,14,10,16,12,23,20,15,21,22,19,18,24])   
                case 12:
                    #solve_puzzle(6,[1,2,4,5,0,6,7,8,3,10,11,12,13,14,9,16,17,18,19,26,15,21,22,24,25,32,20,28,23,30,31,33,27,34,29,35])   
                    solve_puzzle(6,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,0,34,35])
        
        elif r_t == 'd': # stop the program
            break


def solve_puzzle(p_size,puz): 
    """
    solve puzzle
    p_size -> size of clumn/row
    puz -> nXn puzzle
    branch and bound
    """
    tile_number = p_size * p_size # n x n
    finished_puzzle = [x for x in range(tile_number)] # create ordered finished puzzle
    finished_puzzle = finished_puzzle[1:len(finished_puzzle)]
    finished_puzzle.append(0)

    movement = [-p_size,p_size,-1,1] # [move up, move down, left, right]

    not_solved = True # used to get out from the while loop when puzzle is solved

    print(puz)

    if solvable(puz,p_size): # check to see if the puzzle is solvable or not first
        print("solvable\n")
        
        # initialization start
        cost = cost_calc(puz, finished_puzzle)
        zero = zero_posi(puz)
        temp_parent = node(-1,10,[0 for x in range(tile_number)],None,0)
        origin_node = node(0,cost,puz,temp_parent,zero)
        cost_list = min_cost_list()
        cost_list.push_minheaplist(origin_node)
        # initialization done

        keepgoing = True  # used to see if user wants to keep calculating later

        while(not_solved): # loop until puzzle is solved
            parent_node = cost_list.pop_minheaplist() # get the smallest cost node
            p_p_puz = parent_node.get_parent().get_state() # get the puzzle state from the smallest cost node
            
            #check to see if user wants to keep calculation when step is more than around 20
            if keepgoing: 
                if len(cost_list.get_minheaplist()) > 10000: # only asks once
                    keepgoing = False
                    don = input("amount of steps might be more than 20. it could take more than 20 minites to solve it. Do you want to keep calculating? (type 'y' to keep calculating, 'n' to stop) -> ")
                    if don != 'y': # if they want to stop calculation, they can
                        return
            
            for v in range(4): # for all 4 movements

                # check to see if the empty tile tries to go out of puzzle 
                if parent_node.get_zero() + movement[v] < tile_number and parent_node.get_zero() + movement[v] > -1:
                    if not (v==3 and (parent_node.get_zero()%p_size == (p_size-1))):
                        if not (v==2 and (parent_node.get_zero()%p_size == 0)):
                            new_status = copy.deepcopy(parent_node.get_state())
                            new_status[parent_node.get_zero()] = new_status[parent_node.get_zero() + movement[v]]
                            new_status[parent_node.get_zero() + movement[v]] = 0
                            if p_p_puz != new_status: # if the state is not same as the previous state
                                new_node = node(parent_node.get_level() + 1, cost_calc(new_status, finished_puzzle) + parent_node.get_level() + 1, new_status,parent_node, parent_node.get_zero() + movement[v])
                                cost_list.push_minheaplist(new_node)

                                # if puzzle is solved
                                if cost_calc(new_node.get_state(), finished_puzzle) == 0:
                                    ans_node = new_node
                                    not_solved = False
        # print the whole steps
        print_step(ans_node, p_size)

    else:
        print("unsolvable")


def print_step(node, side):
    """
    print all the steps
    """
    status_list = []
    cur_node = node
    npar = np.array(cur_node.get_state()) 
    print("===== solved =====\n")
    print(node.get_level(), " step")
    print(npar.reshape(side,side)) # change 1d list to 2d array
    print("\n")
    while(True): # keep printing until the level of tree gets to 0
        if cur_node.get_level() > 0: 
            cur_node = cur_node.get_parent()
            npar = np.array(cur_node.get_state())
            print(cur_node.get_level(), " step")
            print(npar.reshape(side,side)) # change 1d list to 2d array
            print("\n")
        else:
            break
    print("==================\n\n")
    

def zero_posi(puzzle):
    """
    return index of empty tile
    """
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            return i


def cost_calc(puzzle, finished_puzzle):
    """
    return the amount of misplaced tile
    """
    cost = 0
    for i in range(len(puzzle)):
        if puzzle[i] != finished_puzzle[i]:
            cost += 1
    return cost
        

def createPuzzle(a_side):
    """
    create randomized puzzle
    """
    puz = [x for x in range(a_side * a_side)]
    random.shuffle(puz)
    return puz
        

def solvable(puz,size_p):
    """
    check to see if a puzzle is solvable
    """
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
        if (zero_posi//size_p)%2==0:
            less_posi +=1
    if less_posi%2 == 0:
        return True
    else:
        return False


# call main function
if __name__ == "__main__":
    main()
