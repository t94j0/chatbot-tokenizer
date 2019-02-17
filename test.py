import unittest

from tokenizer import Tokenizer


class MyTest(unittest.TestCase):
    def test_match_basic(self):
        test_string = '!bot abc'
        tokens = Tokenizer(test_string)
        if not tokens.match('!bot <test>'):
            self.fail('Test should match')

    def test_match_not_match(self):
        test_string = '!bot'
        tokens = Tokenizer(test_string)
        if tokens.match('!bot create <test>'):
            self.fail('Test should match')

    def test_match_blank(self):
        test_string = '!bot  abc'
        tokens = Tokenizer(test_string)
        if not tokens.match('!bot <test>'):
            self.fail('Test should match')

    def test_item(self):
        test_string = '!bot abc'
        tokens = Tokenizer(test_string)
        if tokens.match('!bot <test>'):
            items = tokens.items()
            self.assertEqual(items['test'], 'abc')


if __name__ == '__main__':
    unittest.main()
