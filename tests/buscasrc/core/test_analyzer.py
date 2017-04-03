import unittest

from buscasrc.core.analyzer import Analyzer


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = Analyzer()


    def test_prepare_text(self):
        text = "Conan, the barbarian is a great HQ. Conan, #MustRead!"

        self.assertListEqual(self.analyzer.prepare_text(text), [("conan", [0, 4]), ("barbarian", [1]), ("great", [2]), ("hq", [3]), ("mustread", [5])])


    def test_execute_before_filters(self):

        text = "Hello! Can i help you? Some things we have: rice, beans, chicken, ..."

        result = self.analyzer._execute_before_filters(text)

        self.assertEquals(result, "Hello Can i help you Some things we have rice beans chicken ")


    def test_execute_after_filters(self):
        tokens_list = ["After", "all", "we", "will", "resist", "-", "JOHN"]

        result = self.analyzer._execute_after_filters(tokens_list)

        self.assertEquals(result, ["will", "resist", "john"])


    def test_generate_tokens_with_positions(self):
        tokens_list = ["john", "will", "resist", "john"]

        result = self.analyzer._generate_tokens_with_positions(tokens_list)

        self.assertEquals(result, [("john", [0,3]), ("will", [1]), ("resist",[2])])


    def test_get_token_positions(self):
        token = "conan"
        tokens_list= ["conan", "barbarian", "axe", "conan", "sword"]

        self.assertEquals(self.analyzer._get_token_positions(token, tokens_list), [0,3])
