def selection_sort(A):
    """
    Sorts the input array A of length n using selection sort.
    The function sorts in-place in ascending order.

    Time complexity: O(n^2)
    CLRS, exercise 2.2-2
    """
    for i in range(len(A)-1):
        min_v = A[i]
        min_i = i
        for j in range(i+1, len(A)):
            if A[j] < min_v:
                min_v = A[j]
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
