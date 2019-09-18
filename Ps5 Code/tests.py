import unittest
from peg_solve import peg_solve

verbose = False        # CHANGE TO TRUE FOR VISUAL OUTPUT

tests = (
    (
        (
            (0, 0, 0),
            (0, 1, 1),
        ),
        True,
    ),
    (
        (
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
        ),
        True,
    ),
    (
        (
            (0, 1, 0, 0),
            (1, 0, 1, 0),
            (1, 1, 1, 0),
        ),
        True,
    ),
    (
        (
            (0, 1, 0, 1),
            (1, 1, 1, 0),
            (0, 1, 0, 0),
        ),
        False,
    ),
    (
        (
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (1, 1, 1, 0),
            (0, 0, 0, 1),
        ),
        True,
    ),
)

DIRECTIONS = {"N": (-1, 0), "E": ( 0, 1), "S": ( 1, 0), "W": ( 0,-1)}
def make_move(B, m, orientation):
    if m is None: return None
    r, c, d = m
    dr, dc = DIRECTIONS[d]
    R, C = len(B), len(B[0])
    if (0 <= r + 2*dr < R) and (0 <= c + 2*dc < C):
        before, after = (1, 1, 0), (0, 0, 1)
        if orientation is "backward": 
            before, after = after, before
        for i in range(3):
            if B[r + i*dr][c + i*dc] != before[i]:
                return None
        B_ = [[p for p in row] for row in B]
        for i in range(3):
            B_[r + i*dr][c + i*dc] = after[i]
        return tuple(tuple(p for p in row) for row in B_)

def board_str(B):
    return "\n".join("".join("o" if p else "." for p in row) for row in B)

def is_solved(B):
    return sum(sum(row) for row in B) == 1

def check_moves(B, M, verbose = True):
    if verbose: 
        print("Attempting to make %s moves...\n%s" % (len(moves), board_str(B)))
    for m in M:
        if verbose: 
            print("Move (%s, %s) in the %s direction" % m)
        B = make_move(B, m, 'forward')
        if verbose:
            if B:
                print(board_str(B))
            else:
                print("Move NOT valid :(")
    solved = is_solved(B)
    if verbose:
        if solved:
            print("Board solved!")
        else:
            print("Board NOT solved :(")
    return solved

def check(test):
    B, ans = test
    if verbose:
        print("Starting board:\n%s" % board_str(B))
    M = peg_solve(B)
    if ans is False:
        return M is None
    if M is None:
        return False
    return check_moves(B, M, verbose)

class TestHolidayHelper(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[0]))
    def test_02(self): self.assertTrue(check(tests[1]))
    def test_03(self): self.assertTrue(check(tests[2]))
    def test_04(self): self.assertTrue(check(tests[3]))
    def test_05(self): self.assertTrue(check(tests[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
