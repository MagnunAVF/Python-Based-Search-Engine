import unittest

from buscasrc.core.indexer import Indexer
from buscasrc.core.database import Database

class TestIndexer(unittest.TestCase):
    def test_index_document(self):
        database = Database()
        indexer = Indexer(database)

        # tokens extracted from 2 docs:
        tokens_doc1 = [ ("conan", "ABC001", [1, 5 , 7])]
        tokens_doc2 = [ ("barbarian", "DEF002", [3, 10]),
                        ("conan", "DEF002", [2])]

        indexer.index_document(tokens_doc1)
        indexer.index_document(tokens_doc2)

        self.assertEquals(database.inverted_index, {'conan': {'ABC001': [1, 5, 7], 'DEF002': [2]}, 'barbarian': {'DEF002': [3, 10]}})


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

        database = Database()
        indexer = Indexer(database)

        indexer.index_documents(documents)

        self.assertEquals(
            database.inverted_index,
            {
                "barbarian": {"ABC001" : [1]},
                "conan": {"ABC001" : [0, 4] , "DEF999": [2]},
                "great": {"ABC001" : [2]},
                "hello": {"DEF999": [0]},
                "hq": {"ABC001" : [3], "DEF999": [3]},
                "mustread": {"ABC001" : [5]},
                "read": {"DEF999": [1]}
            }
        )


    def test_get_token_positions(self):
        database = Database()
        indexer = Indexer(database)

        token = "conan"
        tokens_list= ["conan", "barbarian", "axe", "conan", "sword"]

        self.assertEquals(indexer.get_token_positions(token, tokens_list), [0,3])

    def test_prepare_document(self):
        database = Database()
        indexer = Indexer(database)

        document = {
            "id": "ABC001",
            "text": "Conan, the barbarian is a great HQ. Conan, #MustRead!"
        }

        self.assertListEqual(indexer.prepare_document(document),
        [
            ("conan","ABC001",[0,4]),
            ("barbarian", "ABC001", [1]),
            ("great", "ABC001", [2]),
            ("hq", "ABC001", [3]),
            ("mustread", "ABC001", [5])
        ])
