import unittest
from most_awesome import most_awesome

tests = (
    (
        (
            [('alpine_ridge', 7), ('rocky_canteen', 5), ('sunrise_ridge', 10), ('east_bluff', 10)],
            [('rocky_canteen', 'alpine_ridge', 21), ('sunrise_ridge', 'rocky_canteen', 43), ('east_bluff', 'rocky_canteen', 18), ('east_bluff', 'alpine_ridge', 44), ('sunrise_ridge', 'alpine_ridge', 23)],
        ),
        65,
    ),
    (
        (
            [('sparrow_point', 14), ('east_cliff', 6), ('alpine_canteen', 8), ('sunrise_peak', 11), ('rocky_summit', 9)],
            [('sunrise_peak', 'alpine_canteen', 50), ('rocky_summit', 'sparrow_point', 71), ('alpine_canteen', 'sparrow_point', 60), ('east_cliff', 'sparrow_point', 43), ('rocky_summit', 'east_cliff', 93), ('alpine_canteen', 'east_cliff', 56), ('rocky_summit', 'sunrise_peak', 48), ('rocky_summit', 'alpine_canteen', 31), ('sunrise_peak', 'sparrow_point', 14), ('sunrise_peak', 'east_cliff', 40)],
        ),
        164,
    ),
    (
        (
            [('cozy_peak', 8), ('north_landing', 17), ('west_landing', 14), ('sparrow_canteen', 8), ('alpine_horizon', 9), ('cozy_point', 8)],
            [('sparrow_canteen', 'west_landing', 142), ('west_landing', 'cozy_peak', 66), ('cozy_point', 'north_landing', 36), ('alpine_horizon', 'north_landing', 110), ('sparrow_canteen', 'north_landing', 88), ('cozy_point', 'alpine_horizon', 135), ('alpine_horizon', 'cozy_peak', 106), ('alpine_horizon', 'sparrow_canteen', 144), ('cozy_point', 'west_landing', 104), ('west_landing', 'north_landing', 15), ('north_landing', 'cozy_peak', 76), ('alpine_horizon', 'west_landing', 139)],
        ),
        298,
    ),
    (
        (
            [('sparrow_horizon', 11), ('north_peak', 12), ('west_horizon', 24), ('cozy_ridge', 9), ('north_cliff', 18), ('sparrow_lodge', 24), ('alpine_peak', 18), ('bobcat_peak', 12)],
            [('alpine_peak', 'north_peak', 139), ('bobcat_peak', 'cozy_ridge', 89), ('north_cliff', 'sparrow_horizon', 14), ('west_horizon', 'sparrow_horizon', 81), ('bobcat_peak', 'west_horizon', 28), ('north_cliff', 'north_peak', 140), ('cozy_ridge', 'sparrow_horizon', 116), ('alpine_peak', 'west_horizon', 57), ('north_cliff', 'west_horizon', 105), ('alpine_peak', 'sparrow_lodge', 126), ('west_horizon', 'north_peak', 179), ('alpine_peak', 'sparrow_horizon', 132), ('north_cliff', 'cozy_ridge', 179), ('cozy_ridge', 'north_peak', 138), ('sparrow_lodge', 'north_peak', 106), ('sparrow_lodge', 'sparrow_horizon', 54), ('bobcat_peak', 'north_cliff', 167), ('bobcat_peak', 'sparrow_lodge', 23), ('cozy_ridge', 'west_horizon', 145), ('sparrow_lodge', 'cozy_ridge', 115)],
        ),
        403,
    ),
    (
        (
            [('east_canteen', 58), ('east_cliff', 28), ('east_bluff', 31), ('sunrise_ridge', 55), ('sunrise_bluff', 45), ('eagle_peak', 46), ('cozy_canteen', 54), ('eagle_canteen', 22), ('north_peak', 21), ('eagle_point', 31), ('rocky_point', 59), ('cozy_cliff', 51), ('east_horizon', 51), ('bobcat_peak', 45), ('alpine_landing', 39), ('eagle_summit', 21), ('sunrise_horizon', 57), ('sparrow_bluff', 48), ('alpine_summit', 43), ('sparrow_horizon', 48)],
            [('alpine_summit', 'eagle_peak', 515), ('eagle_summit', 'bobcat_peak', 171), ('north_peak', 'eagle_peak', 962), ('alpine_summit', 'east_canteen', 299), ('cozy_canteen', 'east_bluff', 235), ('cozy_canteen', 'sunrise_ridge', 506), ('sunrise_horizon', 'cozy_cliff', 851), ('east_horizon', 'east_cliff', 62), ('eagle_summit', 'sunrise_ridge', 631), ('cozy_cliff', 'east_bluff', 189), ('sparrow_bluff', 'east_horizon', 426), ('sparrow_horizon', 'east_canteen', 982), ('sparrow_horizon', 'eagle_point', 370), ('eagle_canteen', 'east_cliff', 578), ('eagle_peak', 'east_canteen', 154), ('cozy_cliff', 'rocky_point', 32), ('sunrise_ridge', 'east_cliff', 792), ('cozy_cliff', 'east_cliff', 352), ('alpine_summit', 'sunrise_horizon', 68), ('eagle_summit', 'eagle_point', 615), ('eagle_peak', 'east_cliff', 590), ('sparrow_bluff', 'sunrise_ridge', 537), ('sunrise_horizon', 'cozy_canteen', 300), ('alpine_landing', 'sunrise_bluff', 734), ('eagle_point', 'east_canteen', 276), ('cozy_cliff', 'sunrise_ridge', 24), ('rocky_point', 'east_cliff', 404), ('sunrise_horizon', 'east_bluff', 930), ('sparrow_bluff', 'north_peak', 889), ('sunrise_horizon', 'rocky_point', 362), ('eagle_summit', 'sunrise_bluff', 482), ('eagle_point', 'sunrise_ridge', 231), ('bobcat_peak', 'east_horizon', 499), ('eagle_canteen', 'east_canteen', 707), ('sparrow_bluff', 'cozy_canteen', 338), ('sparrow_horizon', 'east_horizon', 840), ('sparrow_bluff', 'east_canteen', 106), ('sunrise_horizon', 'north_peak', 594), ('alpine_summit', 'rocky_point', 613), ('rocky_point', 'sunrise_bluff', 627), ('alpine_summit', 'east_cliff', 510), ('bobcat_peak', 'cozy_cliff', 538), ('eagle_canteen', 'sunrise_bluff', 994), ('sparrow_horizon', 'eagle_summit', 428), ('alpine_summit', 'eagle_summit', 966), ('cozy_cliff', 'sunrise_bluff', 781), ('sunrise_horizon', 'sunrise_bluff', 170), ('alpine_landing', 'rocky_point', 947), ('sparrow_horizon', 'sunrise_bluff', 668), ('east_horizon', 'sunrise_bluff', 552), ('rocky_point', 'sunrise_ridge', 842), ('cozy_cliff', 'north_peak', 815), ('bobcat_peak', 'rocky_point', 418), ('alpine_summit', 'sunrise_ridge', 760), ('alpine_landing', 'eagle_peak', 107), ('eagle_canteen', 'eagle_peak', 33), ('sparrow_horizon', 'cozy_canteen', 818), ('eagle_summit', 'east_cliff', 711), ('sunrise_horizon', 'eagle_peak', 232), ('sparrow_bluff', 'alpine_landing', 607), ('alpine_summit', 'sunrise_bluff', 376), ('alpine_summit', 'cozy_cliff', 499), ('eagle_point', 'east_cliff', 627), ('sparrow_horizon', 'east_bluff', 32), ('sparrow_horizon', 'rocky_point', 972), ('alpine_summit', 'east_horizon', 241), ('sparrow_horizon', 'sunrise_ridge', 731), ('sunrise_horizon', 'alpine_landing', 605), ('sparrow_horizon', 'bobcat_peak', 26), ('east_horizon', 'eagle_peak', 247), ('north_peak', 'eagle_canteen', 581), ('eagle_summit', 'alpine_landing', 372), ('eagle_point', 'sunrise_bluff', 924), ('east_horizon', 'east_bluff', 859), ('sunrise_horizon', 'eagle_summit', 781), ('sparrow_horizon', 'eagle_canteen', 226), ('eagle_canteen', 'sunrise_ridge', 362), ('alpine_summit', 'north_peak', 243), ('bobcat_peak', 'east_bluff', 469), ('cozy_cliff', 'east_canteen', 734), ('sunrise_horizon', 'east_horizon', 44), ('east_horizon', 'sunrise_ridge', 481), ('sparrow_horizon', 'eagle_peak', 765), ('eagle_summit', 'cozy_cliff', 487), ('sparrow_bluff', 'eagle_peak', 749), ('east_horizon', 'eagle_point', 167), ('eagle_summit', 'east_bluff', 488), ('sparrow_horizon', 'cozy_cliff', 199), ('north_peak', 'east_cliff', 160), ('alpine_summit', 'eagle_canteen', 125), ('eagle_canteen', 'east_bluff', 225), ('bobcat_peak', 'north_peak', 700), ('sparrow_bluff', 'bobcat_peak', 901), ('north_peak', 'east_canteen', 233), ('eagle_summit', 'east_canteen', 569), ('sparrow_bluff', 'eagle_summit', 279), ('rocky_point', 'cozy_canteen', 379), ('sparrow_horizon', 'alpine_summit', 458), ('sunrise_ridge', 'east_bluff', 622), ('sparrow_bluff', 'sunrise_horizon', 662)],
        ),
        5544,
    ),
)

def check(test):
    args, ans = test
    C, R = args
    H = {}
    for c, h in C:
        H[c] = h
    A = {}
    for c1, c2, a in R:
        A[(c1, c2)] = a
        A[(c2, c1)] = a
    course = most_awesome(C, R)
    total = 0
    if course:
        c1 = course[0]
        for i in range(1, len(course)):
            c2 = course[i]
            if H[c1] <= H[c2]:
                return False
            total += A[(c1, c2)]
            c1 = c2
    return total == ans

class TestClass(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[0]))
    def test_02(self): self.assertTrue(check(tests[1]))
    def test_03(self): self.assertTrue(check(tests[2]))
    def test_04(self): self.assertTrue(check(tests[3]))
    def test_05(self): self.assertTrue(check(tests[4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
