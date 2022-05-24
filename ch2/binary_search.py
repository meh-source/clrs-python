def binary_search(A, v):
    """
    Scans through the sorted input sequence A looking for v.
    A is supposed in increasing order.

    Time complexity: O(lg n)
    CLRS, exercise 2.3-5
    """
    left = 0
    right = len(A)-1

    while left <= right:
        mid = left + (right-left)/2
        if A[mid] == v:
            return mid
        if A[mid] < v:
            left = mid + 1
            continue
        right = mid - 1
    
    return None
