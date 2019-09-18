def annoy(B):
    '''
    Input:  B | list of box dimension triples
    Output: A | list of indicies of max nesting boxes, increasing in dimension
    '''
    A = []
    index = {}

    for i in range(len(B)):
        tup = B[i]
        p = tuple(sorted(list(tup)))
        A.append(p)
        index[p] = i


    new_B = sorted(A, key = lambda x: sum(x))

    cheat = lis(new_B)

    res = []

    for f in cheat:
        res.append(index[f])


    return res


def lis(A):
    x = [1 for _ in A] # memo
    parent = [None for _ in A] # parent pointers
    for i in range(1, len(A)): # solve dynamic program
        for j in range(i):
            if fits_inside(A[j], A[i]) and (x[i] < x[j] + 1):
                x[i] = x[j] + 1
                parent[i] = j
    last = 0 # find largest subproblem
    for i in range(1, len(A)):
        if x[last] < x[i]:
            last = i
    sequence = [] # reconstruct backward sequence
    while last is not None:
        sequence.append(A[last])
        last = parent[last]
    return sequence[::-1] # return reversed sequenc



def fits_inside(b1, b2):
    return all([b1[i] < b2[i] for i in range(3)])