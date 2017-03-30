import unittest

from buscasrc.core.database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.documentFixture = {
            "id": "doc001",
            "text": "Hello! Conan! Have you read Conan HQ? "
        }

    def test_index(self):
        tokens_list = [('hello', [0]), ('conan', [1,3]), ('read', [2]), ('hq', [4])]

        self.database._store_document(self.documentFixture)
        self.database._index_terms(tokens_list, self.documentFixture)

        self.assertEquals(self.database.documents["doc001"], self.documentFixture)
        self.assertEquals(self.database.inverted_index, {'hello': {'doc001': [0]}, 'conan': {'doc001': [1,3]}, 'read': {'doc001': [2]}, 'hq': {'doc001': [4]}})

    def test_store_document(self):
        self.database._store_document(self.documentFixture)

        self.assertEquals(self.database.documents["doc001"], self.documentFixture)


    def test_index_terms(self):
        tokens_list = [('hello', [0]), ('conan', [1,3]), ('read', [2]), ('hq', [4])]

        self.database._index_terms(tokens_list, self.documentFixture)

        self.assertEquals(self.database.inverted_index, {'hello': {'doc001': [0]}, 'conan': {'doc001': [1,3]}, 'read': {'doc001': [2]}, 'hq': {'doc001': [4]}})
