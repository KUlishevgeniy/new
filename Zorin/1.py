A = list(input())
for i in range(0, len(A)):
    for k in range(i + 1, len(A)):
        if int(A[k]) < int(A[i]):
            Q = A[i]
            P = A[k]
            A[i] = P
            A[k] = Q
print(A)