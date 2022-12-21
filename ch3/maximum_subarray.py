def max_subarr_brute_force(A, low, high):
    """
    Brute-force maximum subarray solution: O(n^2), n = high - low + 1
    """
    
    max_sum = -float("inf")
    
    max_low = low
    max_high = high
    
    cur_sum = 0
    
    for i in range(low, high+1):
        for j in range(i, high+1):
            cur_sum += A[j]
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_low = i
                max_high = j
        
        cur_sum = 0
    
    return max_low, max_high, max_sum


def max_subarr_divide_and_conquer(A, low, high):
    """
    Divide-and-conquer maximum subarray solution: O(n lg n), n = high - low + 1
    """
    if low == high:
        return low, low, A[low]

    mid = (low+high) // 2
    left_low, left_high, left_sum = max_subarr_divide_and_conquer(A, low, mid)
    right_low, right_high, right_sum = max_subarr_divide_and_conquer(A, mid+1, high)
    cross_low, cross_high, cross_sum = _find_cross_max_subarray(A, low, mid, high)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
        
    return cross_low, cross_high, cross_sum 


def _find_cross_max_subarray(A, low, mid, high):
    cross_low = low
    cross_high = high
    
    left_sum = -float("inf")
    curr_sum = 0
    for i in range(mid, low-1, -1):
        curr_sum += A[i]
        if curr_sum >= left_sum:
            cross_low = i
            left_sum = curr_sum
    
    right_sum = -float("inf")
    curr_sum = 0
    for i in range(mid+1, high+1):
        curr_sum += A[i]
        if curr_sum >= right_sum:
            cross_high = i
            right_sum = curr_sum
    
    return cross_low, cross_high, left_sum + right_sum


def max_subarr(A, low, high):
    """
    Linear time maximum subarray solution: O(n), n = high - low + 1
    """
    max_sum = -float("inf")
    
    max_low = low 
    max_high = high
    
    cur_low = low 
    cur_sum = 0
    for i in range(low, high+1):
        if cur_sum >= 0:
            cur_sum += A[i]
        else:
            cur_sum = A[i]
            cur_low = i
        
        if cur_sum > max_sum:
            max_sum = cur_sum 
            max_low = cur_low 
            max_high = i 
    
    return max_low, max_high, max_sum


def main():
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    
    low = 0
    high = len(A) - 1
    
    print(max_subarr_brute_force(A, low, high))
    print(max_subarr_divide_and_conquer(A, low, high))
    print(max_subarr(A, low, high))
    
    
if __name__=="__main__":
    main()
