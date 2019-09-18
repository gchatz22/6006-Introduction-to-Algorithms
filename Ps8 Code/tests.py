import unittest
from annoy import annoy

tests = (
    (
        [(36, 26, 27), (45, 32, 39), (49, 34, 43), (46, 29, 41), (35, 40, 25)],
        [4, 3, 2],
    ),
    (
        [(7, 7, 7), (8, 6, 8), (2, 12, 2), (10, 4, 10), (9, 5, 9), (4, 10, 4), (11, 3, 11), (5, 9, 5), (6, 8, 6), (3, 11, 3)],
        [2],
    ),
    (
        [(9, 13, 11), (11, 15, 13), (10, 14, 12), (3, 7, 5), (6, 10, 8), (5, 9, 7), (7, 11, 9), (4, 8, 6), (2, 6, 4), (8, 12, 10)],
        [8, 3, 7, 5, 4, 6, 9, 0, 2, 1],
    ),
    (
        [(53, 73, 97), (79, 62, 95), (83, 57, 92), (67, 90, 98), (96, 75, 63), (61, 66, 82), (78, 65, 56), (60, 87, 86), (94, 70, 68), (81, 54, 99)],
        [6, 5, 1, 3],
    ),
    (
        [(107, 139, 125), (138, 126, 193), (147, 169, 160), (130, 194, 106), (123, 192, 174), (165, 159, 176), (102, 115, 124), (197, 128, 129), (151, 119, 118), (177, 127, 141), (120, 167, 191), (140, 150, 132), (188, 196, 186), (145, 110, 104), (189, 133, 180), (156, 108, 185), (101, 114, 121), (134, 109, 158), (135, 117, 182), (112, 100, 166)],
        [16, 6, 0, 17, 18, 10, 4, 12],
    ),
)

def fits_inside(b1, b2):
    assert len(b1) == len(b2) == 3
    b1, b2 = sorted(b1), sorted(b2)
    return all([b1[i] < b2[i] for i in range(3)])

def check(test):
    B, ans = test
    A = annoy([b for b in B])
    n = len(A)
    for i in range(1, n):
        if not fits_inside(B[A[i - 1]], B[A[i]]):
            return False
    return n == len(ans)

class TestClass(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[0]))
    def test_02(self): self.assertTrue(check(tests[1]))
    def test_03(self): self.assertTrue(check(tests[2]))
    def test_04(self): self.assertTrue(check(tests[3]))
    def test_05(self): self.assertTrue(check(tests[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
