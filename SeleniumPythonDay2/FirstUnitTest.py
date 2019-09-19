'''
Created on Feb 21, 2019

@author: v.ramiya.surendran
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        print("hi")
        pass


    def tearDown(self):
        print("bye")
        pass


    def GoogleSearch(self):
        print("search")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()