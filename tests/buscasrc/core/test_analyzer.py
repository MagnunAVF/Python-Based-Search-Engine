import unittest

from buscasrc.core.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = Analyzer()

    def test_prepare_document(self):
        document = {
            "id": "ABC001",
            "text": "Conan, the barbarian is a great HQ. Conan, #MustRead!"
        }

        self.assertListEqual(self.analyzer.prepare_document(document),
        [
            ("conan","ABC001",[0,4]),
            ("barbarian", "ABC001", [1]),
            ("great", "ABC001", [2]),
            ("hq", "ABC001", [3]),
            ("mustread", "ABC001", [5])
        ])


    def test_prepare_text(self):
        text = "Conan, the barbarian is a great HQ. Conan, #MustRead!"

        self.assertListEqual(self.analyzer.prepare_text(text), ["conan", "barbarian", "great", "hq", "conan", "mustread"])


    def test_execute_before_filters(self):

        text = "Hello! Can i help you? Some things we have: rice, beans, chicken, ..."

        result = self.analyzer.execute_before_filters(text)

        self.assertEquals(result, "Hello Can i help you Some things we have rice beans chicken ")


    def test_execute_after_filters(self):
        tokens_list = ["After", "all", "we", "will", "resist", "-", "JOHN"]

        result = self.analyzer.execute_after_filters(tokens_list)

        self.assertEquals(result, ["will", "resist", "john"])


    def test_generate_structure(self):
        tokens_list = ["john", "will", "resist", "john"]
        document_id = "ABC001"

        result = self.analyzer.generate_structure(tokens_list, document_id)

        self.assertEquals(result,
        [
            ("john", "ABC001", [0,3]),
            ("will", "ABC001", [1]),
            ("resist", "ABC001", [2])
        ])


    def test_get_token_positions(self):
        token = "conan"
        tokens_list= ["conan", "barbarian", "axe", "conan", "sword"]

        self.assertEquals(self.analyzer.get_token_positions(token, tokens_list), [0,3])
