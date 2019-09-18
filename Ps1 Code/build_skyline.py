def build_skyline(B, i = 0, j = None):
    if j is None: j = len(B)
    if j - i == 1:
        (xL, h, xR) = B[i]
        return [(xL, h), (xR, 0)]
    m = (i + j + 1) // 2
    S1 = build_skyline(B, i, m)
    S2 = build_skyline(B, m, j)
    return merge_skylines(S1, S2)


inf = float("inf")


def merge_skylines(S1, S2):
    S1.append((inf, 0))
    S2.append((inf, 0))
    S = []
    i, j, c1, c2, h, x = 0, 0, 0, 0, 0, -inf
    while x < inf:
        x1, h1 = S1[i]
        x2, h2 = S2[j]
        x_ = x1 if x1 < x2 else x2
        if x1 == x_:
            c1 = h1
            i += 1
        if x2 == x_:
            c2 = h2
            j += 1
        h_ = c1 if c2 < c1 else c2
        if h != h_:
            S.append((x_, h_))
        x, h = x_, h_
    return S