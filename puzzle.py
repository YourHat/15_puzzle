"""
empty tile will be represented as 0
"""
import random



def main():
    print("hello")


    puz = createPuzzle(3)
    print(puz)
    if solvable(puz):
        print("solvable")
    else:
        print("unsolvable")












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
        
    print(less_posi)
    if less_posi%2 == 0:
        return True
    else:
        return False


















if __name__ == "__main__":
    main()
