def binary_addition(A, B, n):
    """
    Adds n-bit numbers stored in the input arrays A and B.
    
    Time complexity: O(n)
    CLRS, exercise 2.1-4
    """
    C = [0 for _ in range(n+1)]

    carry = 0
    for i in range(n):
        s = A[i] + B[i] + carry
        if s == 3:
            carry = 1
            C[i] = 1
        elif s == 2:
            carry = 0
            C[i] = 0
        else:
            carry = 0
            C[i] = s
    
    C[n] = carry 
    return C
