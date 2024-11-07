import unittest
from file_job import *

class test(unittest.TestCase):
    def test_true(self):
        self.assertTrue(R("mama"))

    def test_empty_string(self):
        self.assertFalse(R("papa"))
        