import unittest
import Rearrange


class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        s = Rearrange.rearrange("hello World")
        assert s == "Hello world"
