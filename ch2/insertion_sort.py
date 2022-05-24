def insertion_sort(A):
    """
    Sorts the input array A of length n using insertion sort.
    The function sorts in-place in ascending order.

    Time complexity: O(n^2)
    CLRS, section 2.1
    """
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while (j > -1 and A[j] > key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key

def insertion_sort_desc(A):
    """
    Sorts the input array A of length n using insertion sort.
    The function sorts in-place in descending order.

    Time complexity: O(n^2)
    CLRS, exercise 2.1-2
    """
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while (j > -1 and A[j] < key):
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
