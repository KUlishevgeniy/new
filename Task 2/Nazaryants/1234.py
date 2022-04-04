import random
def QSort(A, l, r):
    if l >= r:
        return
    else:
        q = random.choice(A[l:r + 1])
        i = l
        j = r
        while i <= j:
            while A[i] < q:
                i += 1
            while A[j] > q:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
                QSort(A, l, j)
                QSort(A, i, r)
B=[]
QSort(B, 0, (len(B)-1))
print(B)