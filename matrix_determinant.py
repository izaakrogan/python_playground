# determinant matrix

def minor(A,j):
    del A[0]
    A = list(transpose(A))
    del A[j]
    return list(transpose(A))

def det(A):
    if len(A) == 1:
        return A[0][0]
    res = 0
    for j in range(len(A[0])):
        res += (-1)**j*A[0][j]*det(minor(A[:],j))
    return res

A = [[1,19,3,4],[17,5,6,16],[7,71,9,9],[4,3,88,12]]
print(det(A))
