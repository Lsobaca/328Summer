
def find_max_cross(A:list,mid:int,low:int,high:int):
    left_sum = -100000
    sum = 0
    for i in range(mid,low,-1):
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
    
    right_sum = -100000
    sum = 0
    for j in range(mid+1,high):
        sum = sum + A[j]
        if (sum > right_sum):
            right_sum = sum
            
    return max(left_sum + right_sum, right_sum, left_sum)


def find_maximum(A:list,low:int,high:int):
    if high==low:
        return low,high,A[low]

    mid = low + high//2
    left_sum = find_maximum(A,low,mid)
    right_sum = find_maximum(A,mid+1,high)
    cross_sum = find_max_cross(A,low,mid,high)
    
    return max(left_sum,right_sum,cross_sum)

  




lst = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
a = find_maximum(lst,0,len(lst)-1)
print(a)