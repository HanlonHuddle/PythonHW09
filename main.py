"""
    Main entrance for HW09
    Hanrun Li
"""

import unittest
from Repository import Repository

# remember to change this dir for test
CONST_FILEDIR = "/home/hli68/Programming/SSW810/SSW810GHrepo/HW09Data"

class FunctionTest(unittest.TestCase):
    """ verify that Repository works fine """
    def test_dfanalyze(self):
        """ verify dfanalyzer works fine """
        repo = Repository()
        repo.load(CONST_FILEDIR)
        test = ["+-------+-------------+---------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------+\n|  CWID |     Name    |              Complited Cources              |                                    Remaining Required                                    |         Remaining Elective        |\n+-------+-------------+---------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------+\n| 10103 |  Baldwin, C | ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'] |            ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 565', 'SSW 690', 'SSW 695']            |                 []                |\n| 10115 |   Wyatt, X  | ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'] |            ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 565', 'SSW 690', 'SSW 695']            |                 []                |\n| 10172 |  Forbes, I  |            ['SSW 555', 'SSW 567']           |            ['SSW 533', 'SSW 540', 'SSW 564', 'SSW 565', 'SSW 690', 'SSW 695']            |   ['CS 501', 'CS 513', 'CS 545']  |\n| 10175 | Erickson, D |      ['SSW 564', 'SSW 567', 'SSW 687']      |            ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 565', 'SSW 690', 'SSW 695']            |   ['CS 501', 'CS 513', 'CS 545']  |\n| 10183 |  Chapman, O |                 ['SSW 689']                 | ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 564', 'SSW 565', 'SSW 567', 'SSW 690', 'SSW 695'] |   ['CS 501', 'CS 513', 'CS 545']  |\n| 11399 |  Cordova, I |                 ['SSW 540']                 |            ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']            |                 []                |\n| 11461 |  Wright, U  |      ['SYS 611', 'SYS 750', 'SYS 800']      |                 ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674']                  | ['SSW 540', 'SSW 565', 'SSW 810'] |\n| 11658 |   Kelly, P  |                      []                     |            ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']            | ['SSW 540', 'SSW 565', 'SSW 810'] |\n| 11714 |  Morton, A  |            ['SYS 611', 'SYS 645']           |            ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']            | ['SSW 540', 'SSW 565', 'SSW 810'] |\n| 11788 |  Fuller, E  |                 ['SSW 540']                 |            ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']            |                 []                |\n+-------+-------------+---------------------------------------------+------------------------------------------------------------------------------------------+-----------------------------------+", "+------+------------------------------------------------------------------------------------------+-----------------------------------+\n| Dept |                                         Required                                         |              Elective             |\n+------+------------------------------------------------------------------------------------------+-----------------------------------+\n| SFEN | ['SSW 533', 'SSW 540', 'SSW 555', 'SSW 564', 'SSW 565', 'SSW 567', 'SSW 690', 'SSW 695'] |   ['CS 501', 'CS 513', 'CS 545']  |\n| SYEN |            ['SYS 612', 'SYS 671', 'SYS 672', 'SYS 673', 'SYS 674', 'SYS 800']            | ['SSW 540', 'SSW 565', 'SSW 810'] |\n+------+------------------------------------------------------------------------------------------+-----------------------------------+"]
        self.assertEqual(repo.print_table(), test)

def main():
    """ main entrance for part 2 """
    unittest.main(exit=False, verbosity=2)
    # repo = Repository()
    # repo.load(CONST_FILEDIR)
    # print(repo.print_table())
    # repo.print_table()

if __name__ == "__main__":
    main()
