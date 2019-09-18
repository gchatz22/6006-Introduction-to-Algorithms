import unittest
from most_likely_hand import most_likely_hand

tests = (
    (
        (
            'dccbdddbdc',
            2,
        ),
        'bd',
    ),
    # (
    #     (
    #         'abcdefghijklmnopqrstuvwxyz',
    #         13,
    #     ),
    #     'bd',
    # ),
    (
        (
            'aaacfecbacdbdffccaac',
            3,
        ),
        'aac',
    ),
    (
        (
            'kbhcjkhcfjjcjicdkjkgadiiiificeejkfhkeiaheefjgjgfjg',
            4,
        ),
        'chjk',
    ),
    (
        (
            'mdfrztrfqscfgogzglvsfocntdffmappxhepwzwomxlapnkexgvxwjlnhfzibagfuuxjvywjlutdweolxghcmtspkzhztmdugcsb',
            5,
        ),
        'ehppx',
    ),
    (
        (
            'hhdjbdahfegegafdbgejebhcchcbikadjagggkigddkkfekgeekedkgfkcgjbegfbadfjkcihefcdhkdabdbidfhghchjceibjkhbfgfbahafjhhfghikcbhjkebjaiijcjjaebfifafekjijgdcaiaffehegkieedajfjjddghhhdhifhbgkkjcafkdbdjfhdicdikcadiafiebajcjagifffbbkhcgecfikkgjeifdcccefbkfdbihehcckafcdcbadjfgjbidjdhbaekeeacdbjfedicfkcbfdaiggcehgigckjecehfccchchkkifabgicjfbjffhcchaggichcfeacaachagdfjeffccbbaadhkcjfedkaddhaehfkdddecgkbkbhghhdkdcjdfkideaecfhjkabbhihikdfjcibkbhfhafcicibahkdidgibibfagbhaaafggbjkacaideeijhkdihjhbfiehaheeiibfijkhe',
            8,
        ),
        'aaabfggh',
    ),
)

def check(test):
    (D, k), ans = test
    return ans == most_likely_hand(D, k)

class TestHolidayHelper(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
