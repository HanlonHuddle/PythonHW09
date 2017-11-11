"""
    Main entrance for HW09
    Hanrun Li
"""

import unittest
from Repository import Repository

# remember to change this dir for test
CONST_FILEDIR = "/home/hli68/Programming/SSW810/HanrunLiHW09/HW09Data"

class FunctionTest(unittest.TestCase):
    """ verify that Repository works fine """
    def test_dfanalyze(self):
        """ verify dfanalyzer works fine """
        repo = Repository()
        repo.load(CONST_FILEDIR)
        test = [u"+-------+-------------+---------------------------------------------+\n|  CWID |     Name    |              Complited Cources              |\n+-------+-------------+---------------------------------------------+\n| 10183 |  Chapman, O |                 ['SSW 689']                 |\n| 11111 |  HALAHA, P  |                 ['SSW 540']                 |\n| 10172 |  Forbes, I  |            ['SSW 555', 'SSW 567']           |\n| 10175 | Erickson, D |      ['SSW 564', 'SSW 567', 'SSW 687']      |\n| 11399 |  Cordova, I |                 ['SSW 540']                 |\n| 22222 |  LILILI, H  |                 ['SYS 645']                 |\n| 11658 |   Kelly, P  |                 ['SSW 540']                 |\n| 11461 |  Wright, U  |      ['SYS 611', 'SYS 750', 'SYS 800']      |\n| 11714 |  Morton, A  |            ['SYS 611', 'SYS 645']           |\n| 10115 |   Wyatt, X  | ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'] |\n| 11788 |  Fuller, E  |                 ['SSW 540']                 |\n| 10103 |  Baldwin, C | ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'] |\n+-------+-------------+---------------------------------------------+", u'+-------+-------------+------+---------+----------+\n|  CWID |     Name    | Dept |  Cource | Students |\n+-------+-------------+------+---------+----------+\n| 98760 |  Darwin, C  | SYEN | SYS 750 |    1     |\n| 98760 |  Darwin, C  | SYEN | SYS 645 |    2     |\n| 98760 |  Darwin, C  | SYEN | SYS 800 |    1     |\n| 98760 |  Darwin, C  | SYEN | SYS 611 |    2     |\n| 98763 |  Newton, I  | SFEN | SSW 555 |    1     |\n| 98763 |  Newton, I  | SFEN | SSW 689 |    1     |\n| 98765 | Einstein, A | SFEN | SSW 567 |    4     |\n| 98765 | Einstein, A | SFEN | SSW 540 |    4     |\n| 98764 |  Feynman, R | SFEN |  CS 501 |    1     |\n| 98764 |  Feynman, R | SFEN |  CS 545 |    1     |\n| 98764 |  Feynman, R | SFEN | SSW 564 |    3     |\n| 98764 |  Feynman, R | SFEN | SSW 687 |    3     |\n+-------+-------------+------+---------+----------+']
        self.assertEqual(repo.print_table(), test)

def main():
    """ main entrance for part 2 """
    # unittest.main(exit=False, verbosity=2)
    repo = Repository()
    repo.load(CONST_FILEDIR)
    # print(repo.print_table())
    repo.print_table()

if __name__ == "__main__":
    main()
