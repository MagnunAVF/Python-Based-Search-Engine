import unittest

from buscasrc.core.filters.tokens_filters.lowercase_filter import \
    LowercaseFilter


class TestLowercaseFilter(unittest.TestCase):
    def test_filter_tokens(self):
        input_tokens = ["Rice", "Apple", "Conan", "UTF", "barbarian"]

        lowercase_filter = LowercaseFilter(input_tokens)

        self.assertEquals(lowercase_filter.filter_tokens(), [
            "rice", "apple", "conan", "utf", "barbarian"])
