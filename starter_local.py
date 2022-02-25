import unittest
from pobocky import *


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(TestPobocky_D("setup_method"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    return suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(suite())