import unittest
from build_skyline import build_skyline

draw = False # CHANGE TO TRUE FOR VISUAL OUTPUT

tests = (
    (
        ((2, 2, 5),),
        [(2, 2), (5, 0)],
    ),
    (
        ((2, 2, 5), (7, 3, 9)),
        [(2, 2), (5, 0), (7, 3), (9, 0)],
    ),
    (
        ((2, 2, 5), (4, 3, 7)),
        [(2, 2), (4, 3), (7, 0)],
    ),
    (
        ((4, 7, 10), (2, 5, 8), (6, 9, 9), (0, 2, 1), (1, 2, 12)),
        [(0, 2), (2, 5), (4, 7), (6, 9), (9, 7), (10, 2), (12, 0)],
    ),
    (
        ((45, 11, 48), (61, 1, 66), (128, 10, 132), (81, 7, 84), (108, 11, 115), (19, 1, 21), (20, 8, 23), (22, 6, 28), (46, 11, 52), (145, 9, 151), (53, 2, 59), (129, 6, 134), (133, 2, 139), (139, 4, 148), (11, 9, 15), (62, 15, 72), (30, 5, 40), (35, 3, 43), (3, 13, 6), (3, 4, 9), (102, 11, 106), (103, 6, 113), (18, 2, 24), (24, 12, 30), (14, 6, 18), (84, 6, 92), (149, 6, 158), (50, 7, 55), (7, 1, 14), (29, 12, 31), (40, 7, 50), (66, 4, 68), (81, 13, 89), (8, 15, 14), (35, 8, 37), (110, 11, 120), (86, 2, 93), (27, 15, 31), (96, 5, 100), (56, 10, 63)),
        [(3, 13), (6, 4), (8, 15), (14, 9), (15, 6), (18, 2), (20, 8), (23, 6), (24, 12), (27, 15), (31, 5), (35, 8), (37, 5), (40, 7), (45, 11), (52, 7), (55, 2), (56, 10), (62, 15), (72, 0), (81, 13), (89, 6), (92, 2), (93, 0), (96, 5), (100, 0), (102, 11), (106, 6), (108, 11), (120, 0), (128, 10), (132, 6), (134, 2), (139, 4), (145, 9), (151, 6), (158, 0)],
    ),
)

def draw_buildings(B):
    if len(B) == 0: return
    xs, hs = set(), set()
    for (x1, h, x2) in B:
        xs.add(x1)
        xs.add(x2)
        hs.add(h)
    max_x = max(xs) + 1
    max_h = max(hs) + 1
    C = list([' '] * max_x for _ in range(max_h))
    for (xL, h, xR) in B:
        for x in range(xL, xR + 1):
            if x in [xL, xR]:
                C[h][x] = '+'
            else:
                C[h][x] = '-'
        for h in range(h):
            for x in [xL, xR]:
                if h == 0:
                    C[h][x] = '+'
                else:
                    C[h][x] = '|'
    for line in reversed(C):
        print(''.join(line))

def draw_skyline(S):
    if len(S) == 0: return
    xs, hs = set(), set()
    for (x, h) in S:
        xs.add(x)
        hs.add(h)
    max_x = max(xs) + 1
    max_h = max(hs) + 1
    C = list([' '] * max_x for _ in range(max_h))
    x_, _ = S[0]
    h_ = 0
    for (x, h) in S:
        for i in range(x_, x + 1):
            if i in [x, x_]:
                C[h_][i] = '+'
            else:
                C[h_][i] = '-'
        (h1, h2) = (h, h_) if (h < h_) else (h_, h)
        for j in range(h1, h2 + 1):
            if j == h1 or j == h2:
                C[j][x] = '+'
            else:
                C[j][x] = '|'
        x_, h_ = x, h
    for line in reversed(C):
        print(''.join(line))

def check(test):
    B, S = test
    ans = build_skyline(B)
    if draw:
        print("Input:")
        draw_buildings(B)
        print("Solution:")
        draw_skyline(S)
        print("Student Output:")
        draw_skyline(ans)
    return ans == S

class TestSearch2D(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[0]))
    def test_02(self): self.assertTrue(check(tests[1]))
    def test_03(self): self.assertTrue(check(tests[2]))
    def test_04(self): self.assertTrue(check(tests[3]))
    def test_05(self): self.assertTrue(check(tests[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
