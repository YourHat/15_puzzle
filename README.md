Assignment 5. Programming Assignment: Branch and bound method for the 15-puzzle ((n^2 - 1)-puzzle).
Due: 04/20/23, in dropbox.
Read: HSR book Ch. 8, 8.1.2-3, and slides VII (based on Papadimitriou and Steiglitz) 

Programming assignment: 15-puzzle.
Implement Least Cost (LC) search. The cost for a node x in the state space tree is the length of the path from the root to the nearest goal node (if any) in the subtree with root x. Use the approximate cost 
C(x) = f(x) + G(x), 
where f(x) = the length of the path from the root to node x, 
and G(x) = the number of non-blank tiles not in their goal position. 
At least G(x) moves will have to be made to transform state x to the goal state, but more may be needed. Refer to the state space tree of Figure 8.3. 
At each step, a node of least cost is selected for expansion, until the goal state is reached. For an efficient selection, use a min-heap keyed with the costs. 
Run your program for five initial states that lead to a goal state. 
Extra credit 1: Implement the criterion of Theorem 8.1 to determine if the goal state is reachable from a given initial state. 
Extra credit 2: generalize to the (n^2 - 1)-puzzle.
