import unittest

from buscasrc.core.searcher import Searcher
from buscasrc.core.database import Database
from buscasrc.core.analyzer import Analyzer


class TestSearcher(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.searcher = Searcher(self.database, Analyzer())

    def test_search_documents(self):
        self.database.inverted_index = {
            'fox': {'doc001': [0], 'doc002': [0], 'doc004': [1]},
            'run': {'doc001': [1]},
            'dog': {'doc003': [0]},
            'black': {'doc003': [1]},
            'horse': {'doc004': [0]},
            'white': {'doc004': [2]},
            'red': {'doc002': [1]}
        }
        self.database.documents = {
            'doc001': "The fox run.",
            'doc002': "The fox is red.",
            'doc003': "The dog is black.",
            'doc004': "The horse and the fox are white",
        }

        result_docs = self.searcher.search_documents("The white fox")
        print(result_docs)
        self.assertEquals(sorted(result_docs), [
            "The fox is red.", "The fox run.",
            "The horse and the fox are white"])
