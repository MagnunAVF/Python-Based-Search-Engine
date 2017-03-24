import unittest

from buscasrc.search_engine import SearchEngine


class TestSearchEgine(unittest.TestCase):
    def test_example(self):
        search_engine = SearchEngine("teste")

        self.assertEquals(search_engine.value, "teste")
