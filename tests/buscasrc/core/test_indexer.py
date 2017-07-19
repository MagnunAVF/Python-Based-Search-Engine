import unittest

from buscasrc.core.indexer import Indexer
from buscasrc.core.database import Database
from buscasrc.core.analyzer import Analyzer


class TestIndexer(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.indexer = Indexer(self.database, Analyzer())

    def test_index_document(self):
        document = {
            "id": "DEF002",
            "text": "Hello! Conan! Have you read Conan HQ? "
        }

        self.indexer.index_document(document)

        self.assertEquals(self.database.inverted_index, {
            'hello': {'DEF002': [0]},
            'conan': {'DEF002': [1, 3]},
            'read': {'DEF002': [2]},
            'hq': {'DEF002': [4]}})

    def test_index_documents(self):
        documents = [
            {
                "id": "ABC001",
                "text": "Conan, the barbarian is a great HQ. Conan, #MustRead!"
            },
            {
                "id": "DEF999",
                "text": "Hello! Have you read Conan HQ? "
            }
        ]

        self.indexer.index_documents(documents)

        self.assertEquals(
            self.database.inverted_index,
            {
                "barbarian": {"ABC001": [1]},
                "conan": {"ABC001": [0, 4], "DEF999": [2]},
                "great": {"ABC001": [2]},
                "hello": {"DEF999": [0]},
                "hq": {"ABC001": [3], "DEF999": [3]},
                "mustread": {"ABC001": [5]},
                "read": {"DEF999": [1]}
            }
        )
