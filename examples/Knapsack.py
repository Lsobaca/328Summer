


def knapsack(weight:int,n:int,elements:list):
    B = [[0 for _ in range(weight+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(weight+1):
            if i == 0 or j == 0:
                B[i][j] = 0
            
    
    
    
    return B




lst = [[2,3],
        [3,4],
        [4,5],
        [5,6]]
n = len(lst)
max_weight = 5
print(knapsack(max_weight,n,lst))