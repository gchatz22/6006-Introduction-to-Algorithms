import unittest
from HolidayHelper import HolidayHelper

draw = False # CHANGE TO TRUE FOR VISUAL OUTPUT

tests = (
    (
        ((10, 'bad'), (4, 'bad'), (7, 'good'), ('q', 3, 6)),
        [-1],
    ),
    (
        ((10, 'bad'), (6, 'good'), (8, 'good'), (8, 'bad'), (5, 'good'), ('q', 1, 9)),
        [1],
    ),
    (
        ((15, 'good'), (12, 'good'), (7, 'good'), (11, 'good'), (17, 'bad'), (14, 'bad'), (18, 'bad'), (11, 'bad'), (2, 'good'), (4, 'bad'), ('q', 6, 15)),
        [1],
    ),
    (
        ((31, 'good'), (25, 'bad'), (33, 'good'), (38, 'bad'), (50, 'bad'), (40, 'bad'), (46, 'bad'), (9, 'good'), (45, 'good'), (31, 'bad'), ('q', 1, 49), (41, 'bad'), (43, 'bad'), (47, 'good'), (11, 'bad'), (35, 'bad'), (8, 'good'), (21, 'good'), (21, 'bad'), (48, 'good'), (26, 'good'), ('q', 11, 28)),
        [-2, -2],
    ),
    (
        ((70, 'bad'), (80, 'good'), (85, 'good'), (81, 'bad'), (17, 'bad'), (62, 'bad'), (87, 'bad'), (75, 'good'), (41, 'bad'), (11, 'bad'), (90, 'bad'), (13, 'bad'), (52, 'good'), (21, 'bad'), (57, 'good'), ('q', 5, 27), ('q', 54, 73), (99, 'bad'), (16, 'bad'), (90, 'good'), (60, 'bad'), (22, 'good'), (99, 'good'), (76, 'good'), (6, 'bad'), (44, 'bad'), (75, 'bad'), (76, 'bad'), (81, 'bad'), (73, 'good'), (43, 'good'), (39, 'bad'), ('q', 64, 71), ('q', 45, 82)),
        [-4, -1, -1, -2],
    ),
)

def check(test):
    ops, ans = test
    database = HolidayHelper() 
    i = 0
    for op in ops:
        if draw: 
            print('\nDatabase: \n%s\n' % database)
        if op[0] == 'q':
            _, t1, t2 = op
            sol = database.range_imbalance(t1, t2)
            if draw: 
                print(' our range_imbalance(%s,%s): %s' % (t1, t2, ans[i]))
                print('your range_imbalance(%s,%s): %s' % (t1, t2, sol))
            if sol != ans[i]:
                ans.append(sol)
                return False
            i += 1
        else:
            b, g = op
            database.update_kid(b, g)
            if draw: 
                print("update_kid(%s,'%s')" % (b, g))
    return True

class TestHolidayHelper(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
