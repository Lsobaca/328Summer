



# internet and book 
def knapsack2(weight:int,n:int,elements:list):
    B = [[0 for _ in range(weight+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for w in range(weight+1):
            if i == 0 or w == 0:
                B[i][w] = 0

            elif elements[i-1][0] <= w:
                B[i][w] = max(elements[i-1][1] +
                     B[i-1][w - elements[i-1][0]],B[i-1][w])
            else:
                  B[i][w] = B[i-1][w] # w_i > Weight
    
    
    
    return B[n][weight]



# internet copy
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]


# book example
def knapsack3(W,n,elements):
    B = [[0 for _ in range(W+1)]for _ in range(n+1)]
    for item in range(n+1):
        for w in range(W+1):
            if item == 0 or w == 0:
                B[item][w] = 0
            elif elements[item-1][0] <= w:
                if elements[item-1][1] + B[item-1][w-elements[item-1][0]] > B[item-1][w]:
                    B[item][w] = elements[item-1][1] + B[item-1][w-elements[item-1][0]]
                else:
                    B[item][w] = B[item-1][w]
            else:
                B[item][w] = B[item-1][w]

    return B

# lst[wieght][benifit]
lst = [ [2,3],
        [3,4],
        [4,5],
        [5,6]]
n = len(lst)
max_weight = 5
print(knapsack2(max_weight,n,lst))
kekee = knapsack3(max_weight,n,lst)
for i in kekee:
    print(i)

val = [3,4,5,6]
wt = [2,3,4,5]
n = len(val)
W = 5
print(knapSack(W,wt,val,n))

