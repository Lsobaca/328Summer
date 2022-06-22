




def LCS(A:list,B:list) -> int:
    """Longest Common Subsequence. the algo is close to what the book.

    Args:
        A (list): a list of str
        B (list): a lsit of str

    Returns:
        C: the size of the subsequence 
    """
    m = len(A)
    n = len(B)

    C = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                C[i][j] = 0
            elif A[i-1] == B[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else :
                C[i][j] = max(C[i-1][j], C[i][j-1])
    
    return C[n][m]





lst = 'AGGTA'
lst2= 'GXTXAYBVE'
print(LCS(lst,lst2))
