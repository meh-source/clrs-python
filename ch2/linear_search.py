def linear_search(A, v):
    """
    Scans through the input sequence A looking for v.
    
    Time complexity: O(n)
    CLRS, exercise 2.1-3
    """

    for i in range(len(A)):
        if A[i] == v:
            return i
    
    return None
