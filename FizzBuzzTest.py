import unittest 
from unittest.mock import patch
from io import StringIO

from FizzBuzz import FizzBuzz
class TestFizzBuzz(unittest.TestCase):

    @patch('sys.stdin', StringIO('20'))
    @patch('sys.stdout', new_callable= StringIO)
    def test_output(self, stdout):
        #Run the function
        FizzBuzz()

        #Save what we are expecting
        expected= "Choose a number greater than 0: Fizzbuzz\n1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzbuzz\n16\n17\nFizz\n19\nThere are 5 occurences of Fizz\nThere are 2 occurences of Buzz\nThere are 2 occurences of Fizzbuzz\nThe sum of all numbers is 112\n"

        #Check values
        self.assertEqual(stdout.getvalue(), expected)

    @patch('sys.stdin', StringIO('10'))
    @patch('sys.stdout', new_callable= StringIO)
    def test_datatype(self, stdout):
        #Run the function
        x = FizzBuzz()

        #Check values
        self.assertIsInstance(x, list)

    
if __name__ == '__main__':
    unittest.main()