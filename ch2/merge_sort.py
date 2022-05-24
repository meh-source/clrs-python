def merge_sort(A, p, r):
    """
    Sorts the input array A of length n using merge sort.
    The function sorts in-place in ascending order.

    Time complexity: O(n lg n)
    CLRS, section 2.3.1
    """
    if p < r:
        q = p + (r-p)/2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0 for _ in range(n1+1)]
    R = [0 for _ in range(n2+1)]
    
    R[n2] = float('inf')
    L[n1] = float('inf')

    for i in range(n1):
        L[i] = A[p+i]

    for i in range(n2):
        R[i] = A[q+i+1]
    
    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1    
