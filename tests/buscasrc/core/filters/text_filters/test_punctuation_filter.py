import unittest

from buscasrc.core.filters.text_filters.punctuation_filter import \
    PunctuationFilter


class TestPunctuationFilter(unittest.TestCase):
    def test_filter_text(self):
        input_text = "Hello! Can i help you? Some things we have: " \
                    "rice, beans, chicken, ..."

        punctuation_filter = PunctuationFilter(input_text)

        self.assertEquals(punctuation_filter.filter_text(),
                          "Hello Can i help you Some things we have rice beans"
                          " chicken ")
