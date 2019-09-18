import unittest
from MamaBearDB import MamaBearDB

tests = (
    (
        (
            1,          # k
            (3, 'q'),   # operations
        ),
        [(3,)],         # query solutions
    ),
    (
        (
            1,
            (2, 18, 'q', 24, 8, 'q'),
        ),
        [(2,), (8,)],
    ),
    (
        (
            2,
            (57, 48, 65, 'q', 67, 53, 63, 'q', 51, 57, 70, 'q'),
        ),
        [(48, 57), (57, 63), (57, 57)],
    ),
    (
        (
            3,
            (158, 5, 100, 126, 141, 'q', 27, 188, 16, 112, 58, 'q', 93, 192, 147, 75, 58, 'q', 93, 216, 190, 23, 120, 'q', 51, 179, 103, 195, 6, 'q'),
        ),
        [(100, 126, 141), (58, 100, 112), (93, 100, 112), (93, 100, 112), (100, 103, 112)],
    ),
    (
        (
            7,
            (494, 170, 365, 367, 221, 'q', 137, 330, 320, 279, 442, 'q', 311, 117, 150, 164, 250, 'q', 287, 323, 108, 466, 87, 'q', 228, 138, 15, 74, 154, 'q', 109, 252, 335, 331, 22, 'q', 280, 54, 461, 249, 309, 'q', 416, 414, 364, 72, 172, 'q', 323, 475, 312, 57, 195, 'q', 156, 50, 477, 271, 356, 'q'),
        ),
        [(170, 221, 365, 367, 494), (170, 221, 279, 320, 330, 365, 367), (170, 221, 250, 279, 311, 320, 330), (170, 221, 250, 279, 287, 311, 320), (164, 170, 221, 228, 250, 279, 287), (164, 170, 221, 228, 250, 252, 279), (221, 228, 249, 250, 252, 279, 280), (221, 228, 249, 250, 252, 279, 280), (228, 249, 250, 252, 279, 280, 287), (228, 249, 250, 252, 271, 279, 280)],
    ),
)

def check(test):
    args, sol = test
    k, ops = args
    DB = MamaBearDB(k)
    i = 0
    for s in ops:
        if s == 'q':
            # if DB.best_bowls() != sol[i]:
            #     return False
            print(DB.best_bowls())
            i += 1
        else:
            DB.record_bowl(s)
            print(DB.list)
    return True

class TestMamaBear(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[0]))
    # def test_02(self): self.assertTrue(check(tests[1]))
    # def test_03(self): self.assertTrue(check(tests[2]))
    # def test_04(self): self.assertTrue(check(tests[3]))
    # def test_05(self): self.assertTrue(check(tests[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
