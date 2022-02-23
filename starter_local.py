import unittest
from pobocky import TestPobocky_D




#from threading import Thread
#Thread(target=TestPoznavacky_D(unittest.TestCase))

#class TestAll(unittest.TestCase):
#    TestPobocky_D(unittest.TestCase)


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(TestPobocky_D("setup_method"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())