import unittest
from file_job import *

class test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(R("mama"))
        self.assertTrue(R("nn"))

    def test_empty_string(self):
        self.assertFalse(R("paa"))
        self.assertFalse(R("  "))
        