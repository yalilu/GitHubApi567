#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:33:46 2019

@author: luyali
"""

import unittest
from homework04 import get_info_api

class TestApi(unittest.TestCase):
    def testApi(self): 
        self.assertEqual(get_info_api('yalilu'),'Right')
        
    def testApi(self): 
        self.assertEqual(get_info_api('mhassany'),'Right')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()



