import unittest

from buscasrc.search_engine import SearchEngine


class TestSearchEgine(unittest.TestCase):
    def setUp(self):
        self.search_engine = SearchEngine()

    def test_index_and_search_document(self):
        doc1 = {'id': 'doc1', 'text': 'Hello obama!'}
        self.search_engine.index(doc1)
        doc2 = {'id': 'doc2', 'text': 'Hello president Obama!'}
        self.search_engine.index(doc2)
        doc3 = {'id': 'doc3', 'text': 'President Trump will fall.'}
        self.search_engine.index(doc3)
        doc4 = {'id': 'doc4', 'text': 'Nanoc the barbarian'}
        self.search_engine.index(doc4)

        result_docs = self.search_engine.search("President Obama")
        result_docs.sort()

        self.assertEquals(result_docs, [
                'Hello obama!',
                'Hello president Obama!',
                'President Trump will fall.']
        )
