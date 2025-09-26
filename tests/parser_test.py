import unittest

from src.parser import Parser
from tests.mock.mock_input import MockInput
from tests.mock.mock_output import MockOutput


class ParserTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.out = MockOutput()
        self.parser = Parser(
            inp=MockInput(),
            out=self.out,
        )

    def test_parser(self):
        self.parser.parse_news()
        self.assertEqual(len(self.out.data), 14)