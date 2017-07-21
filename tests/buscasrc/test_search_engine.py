import unittest

from buscasrc.search_engine import SearchEngine


class TestSearchEgine(unittest.TestCase):
    def setUp(self):
        self.search_engine = SearchEngine()

    def test_index_and_search_document(self):
        docs = [
            {'id': 'doc1', 'text': 'Hello obama!'},
            {'id': 'doc2', 'text': 'Hello president Obama!'},
            {'id': 'doc3', 'text': 'President Trump will fall.'},
            {'id': 'doc4', 'text': 'Nanoc the barbarian'}]

        for doc in docs:
            self.search_engine.index(doc)

        result_docs = self.search_engine.search("President Obama")

        self.assertEquals(sorted(result_docs), [
                'Hello obama!',
                'Hello president Obama!',
                'President Trump will fall.']
        )
